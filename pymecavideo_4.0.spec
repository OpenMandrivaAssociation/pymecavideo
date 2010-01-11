%define name	pymecavideo
%define version	4.0
%define release	%mkrel 1
%define title	pymecavideo

Name:		%{name} 
Summary:	Pymecavideo permet de tracer les trajectoires décrites par un  ou plusieurs points d'un objet en utilisant une video
Version:	%{version} 
Release:	%{release} 
Source:		%{name}-%{version}.tar.gz

URL:		http://outilsphysiques.tuxfamily.org/pmwiki.php/Oppl/Pymecavideo
Group:		Sciences/Physics
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  libqt4-devel
BuildRequires:  python-devel
Requires:	python-qt4
Requires:       ffmpeg
Requires:	vlc

BuildRoot:	%{_tmppath}/%{name}-buildroot 
License:	GPLv3 


%description
pymecavideo permet de tracer point par point la trajectoire de point ainsi que choisir un référentiel particulier pour étudier la trajectoire dans celui-ci. Les données ainsi recueillies peuvent être exportées dans un logiciel de traitement.

%prep 
%setup -q

%build 
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
#mkdir %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}

#python setup.py install --root %{buildroot}
python setup.py install --prefix=%{buildroot}%{_prefix} --install-lib=%{buildroot}%{_libdir}/python2.6/site-packages

#cp -Rp * %{buildroot}

mkdir -p %{buildroot}%{_bindir}
#icons
mkdir -p %{buildroot}%{_liconsdir}
mkdir -p %{buildroot}%{_iconsdir}
mkdir -p %{buildroot}%{_miconsdir}
cp icones/%{name}-48.png %{buildroot}%{_iconsdir}/%{name}.png
cp pymecavideo.svg %{buildroot}%{_iconsdir}/
mkdir %{buildroot}%{_libdir}/python2.6/site-packages/%{name}/help/
cp help/* %{buildroot}%{_libdir}/python2.6/site-packages/%{name}/help/

cp %{buildroot}%{_libdir}/python2.6/site-packages/%{name}/icones/%{name}-48.png %{buildroot}%{_miconsdir}/%{name}.png

cp %{buildroot}%{_libdir}/python2.6/site-packages/%{name}/icones/%{name}-48.png %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cp pymecavideo.desktop %{buildroot}%{_datadir}/applications

#help
mkdir -p %{buildroot}/%_docdir/HTML/fr/pymecavideo/
cp -r %{buildroot}%{_libdir}/python2.6/site-packages/%{name}/help/*.png %{buildroot}/%_docdir/HTML/fr/pymecavideo/
cp -r %{buildroot}%{_libdir}/python2.6/site-packages/%{name}/help/*.css %{buildroot}/%_docdir/HTML/fr/pymecavideo/
cp -r %{buildroot}%{_libdir}/python2.6/site-packages/%{name}/help/help-fr.* %{buildroot}/%_docdir/HTML/fr/pymecavideo/

cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
python %{_libdir}/python2.6/site-packages/pymecavideo/__init__.py
EOF

chmod a+x %{buildroot}%{_bindir}/%{name}
%clean 
rm -rf %{buildroot} 

%files
%{_bindir}
%{_libdir}
#%{_liconsdir}
#%{_iconsdir}
#%{_miconsdir}
%{_datadir}
#%{_prefix}/*
%defattr(-, root, root,755)
