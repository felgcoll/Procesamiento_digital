%Directorio a recorrer
path='C:\Users\usuario\Desktop\Procesamiento\Blob-2\Shim_L100_U8-63\';
files = dir (strcat(path,'*.png'));
L = length (files);

%Directorio a guardar los resultados
folder = 'C:\Users\usuario\Desktop\Procesamiento\Skel\Shim_L100_U8-63\'; 
 
%Iteración sobre el diccionario que contiene los archivos a procesar  
for i=1:L
    
    %Se abre el fichero y el nuevo a guardar
    img = strcat(path,'',files(i).name);
    img_new = strcat(folder,'',files(i).name);
    bn = imread(img);

    %Transforma de 3D a 2D el archivo
    BN = im2bw(bn);

    %Implementación de la operación: 'Esqueletonización'
    BW3 = bwmorph(BN,'thin', Inf);
    
    %Implementación de la operación : 'Eliminación de los 'spurs''      
    %con sus respectivas iteraciones
    bw3 = bwmorph(BW3, 'spur', Inf);

    %Guardar los resultados
    imwrite(BW3,img_new);

end

