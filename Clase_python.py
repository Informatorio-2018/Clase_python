
# ALGUNOS COMANDOS DE GIT

# git config --global user.name "nombre"  * para configurar el nombre de usuario.
# git config --global user.name           * para ver el nombre de usuario.
# git config --global user.email          * para agregar nuestro correo.
# git config --global color.ui true       * configura los colores.
# git config --global --list              * nos va a mostrar el listado de las configuraciones.

# git config --global http.proxy http://direccion_ip_proxy:puerto  * habilitar el proxy
# git config --global https.proxy         * muestra la configuración 
# git config --global --unset https.proxy

# ---------------
# clear						  * limpia la pantalla.
# exit						  * salir de git bash.	
# git init					  * marca el inicio de monitoreo
# git status					  * muestra el estado de la carpeta de trabajo
# git add "-A" o ".""           * agrega todo lo que hay en el directorio
# git add "archivo.extención"   * agrega solo el archivo indicado
# git commit -m "mensaje"		  * guarda los cambios realizados
# git commit -m "Mensaje corregido" --amend * modifica el mensaje del último commit
# git log   					  * nos muestra los commit creados
# git log > "archivo.txt"       * nos genera un .txt con los commits realizados.
# git checkout "id_commit"	  * viajamos a las distintas versiones  
# git checkout master			  * nos lleva a la última version
# git branch					  * nos muestra las ramas disponibles.
# git branch 'nombre_rama'	  * crea una nueva rama, y nos posiciona en ella.
# git checkout 'nombre_rama'    * viaja hacia la rama indicada.
# git branch -d 'nombre_rama'   * elimina la rama, si la rama tiene archivos sin fucionar, 									nos va a devolver un error.
# git branch -D 'nombre_rama'   * para forzar la eliminación de la rama con archivos sin 									    fusionar.
# git checkout master			  * también nos lleva a la rama principal.
# git merge 'nombre_rama'       * fuciona las ramas, hay que estar en la rama que absorverá a 								la rama indicada con marge.
# git checkout -b 'nombre_rama' * crea una nueva rama y se ubica en ella.

# git remote add origin 'ruta'
# git push                      * es para subir a un repositorio remoto, github
# git pull 					  * trae los cambios que han realizado 
# git clone 					  * copia del proyecto remoto
# git fetch origin 'rama_remota':'rama_local'  * trae una rama remota
