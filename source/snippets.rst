Code Snippets
=============


Python
------

Petit script pour générer une doc Sphinx et la publier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
   :emphasize-lines: 3,5

   #!/usr/bin/python
   import os

   here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

   os.system("make html")
   os.system("rsync -v -r --delete %s root@k3z.fr:/home/k3zfr/wiki/" % here('build/html/'))


Système
-------

Mettre à jour Ruby avec Brew sur Mac OS X Lion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installer `homebrew <http://mxcl.github.com/homebrew/>`_, puis installer Ruby.

.. code::

    $brew install ruby

Ensuite il faut modifier votre PATH pour permettre au système d'éxécuter la version installée par Brew et trouver les gems installés. À adapter selon votre environnement et la version de ruby installée (brew info ruby).

.. code::

    # ~/.bashrc
    export PATH=/usr/local/bin:/usr/local/Cellar/ruby/1.9.3-p385/bin:$PATH

Avec la commande which, on peut connaître l'ordre de recherche de Ruby par le système.

.. code::

    $ which -a ruby
    …
    /usr/local/bin/ruby
    …
    /usr/bin/ruby
    …


Synchroniser deux dossiers en FTP avec lftp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lorsqu’on ne dispose pas d’un acces SSH mais seulement FTP et qu’il faut synchroniser le contenu de deux dossiers, lftp et la commande "mirror" pourra se substituer efficacement à rsync.

Exemple avec ce petit script :

.. code::

  # script.lftp
  debug
  set ftp:list-options -a;
  set cmd:fail-exit yes
  set ftp:ssl-allow no
  set ftp:passive-mode on
  open ftp://$USER:$PASSWORD@$HOST:$PORT;
  lcd /local/folder;
  cd /remote/folder;
  mirror


Lancer le script :

.. code::

  $ lftp -f script.lftp

`Lien vers la documentation <http://doc.ubuntu-fr.org/lftp>`_, pour connaître les subtilités de la commande "mirror" (mirror -r, mirrot -e…).


Mysql
-----

Rechercher/remplacer une chaine dans une table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

  UPDATE
    table_name
  SET
    col = REPLACE(col, 'search_string', 'replace_string')
  WHERE
    col LIKE('%search_string%')


Order by à partir des valeurs d’un champ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

  create temporary table test (id serial, field text);
  insert into test(field) values
    ('GBP'), ('EUR'), ('BBD'), ('AUD'), ('CAD'), ('USD'),
    ('GBP'), ('EUR'), ('BBD'), ('AUD'), ('CAD'), ('USD');
  select * from test
  order by field!='USD', field!='EUR', field!='BBD',
    field!='AUD', field!='CAD', field!='GBP', id asc;
