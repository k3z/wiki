Vim : configuration, ressources
===============================

Vim est un éditeur très puissant à condition d’adopter sa philosophie. Pour quelqu’un qui pratique Textmate ou Sublime Text depuis quelques années cet outil est très déroutant. Voici une compilation de mon kit de survie pour faciliter son apprentissage.

Extensions
----------

* `Pathogen : permet d'installer facilement des extensions <https://github.com/tpope/vim-pathogen>`_.
* `Sensible : configation par défaut facilitant l'usage de Vim <https://github.com/tpope/vim-sensible>`_.
* `Colour schemes by Dayle Rees <https://github.com/daylerees/colour-schemes>`_.
* `Nerdtree : explorateur de fichiers <https://github.com/scrooloose/nerdtree>`_.
* `NERD Commenter : permet de commenter/decommenter facilement des lignes, portions de code <https://github.com/scrooloose/nerdcommenter>`_ (`voir aussi TComment <https://github.com/tomtom/tcomment_vim>`_).
* `SnipMate : complétion à la mode de Textmate avec la touche \<tab\> <https://github.com/msanders/snipmate.vim>`_.


Raccourcis clavier mantras
--------------------------

:ctrl-ww: permet de passer d’une vue splitée à l'autre (ctrl-w + h,j,k,l permet de spécifier la direction).
:$: Déplace le curseur à la fin de la ligne.
:A: Déplace le curseur à la fin de la ligne en mode édition.
:G: Déplace le curseur au début de la dernière ligne du document.

NerdTree
^^^^^^^^

:m: Ajouter, supprimer, renommer un répertoire ou un fichier.
:i: Ouvre un fichier dans un buffer avec un split horizontal.
:s: Ouvre un fichier dans un buffer avec un split vertical.

Tips
----

* `Top 10 Pitfalls When Switching to Vim <http://net.tutsplus.com/articles/general/top-10-pitfalls-when-switching-to-vim/>`_.
* `How I boosted my Vim <http://nvie.com/posts/how-i-boosted-my-vim/>`_.

.vimrc (17/02/2013)
------

.. code::

    execute pathogen#infect()

    " vim Auto detect syntax highlighting
    syntax on
    filetype plugin indent on

    " My favorite color sheme
    colorscheme Laravel

    " Show line number
    " set number

    " Activate smart indentation and set spaces insteed of tabs
    set smartindent
    set tabstop=4
    set shiftwidth=4
    set expandtab ts=4 sw=4 ai

    " Avoid backspace and delete problem
    set backspace=2

    " Remove automaticaly trailing spaces in specifier FileTypes
    autocmd FileType css,html,rst,js,php autocmd BufWritePre <buffer> :%s/\s\+$//e

    " Allow NERDTree to display hidden files
    let NERDTreeShowHidden=1

    " Display the cursor position on the last line of the screen or in the status
    " line of a window
    set ruler

    " Always display the status line, even if only one window is displayed
    set laststatus=2

    " Instead of failing a command because of unsaved changes, instead raise a
    " dialogue asking if you wish to save changed files.
    set confirm

    " Use visual bell instead of beeping when doing something wrong
    set visualbell

    " Enable use of the mouse for all modes
    set mouse=a
    "
    " Set the command window height to 2 lines, to avoid many cases of having to
    " press <Enter> to continue"
    set cmdheight=2
