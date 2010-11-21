%define name	pymecavideo
%define version	5.2
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
%setup -q -n %version

%build 
#make
python setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
#mkdir %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}

#python setup.py install --root %{buildroot}
python setup.py install --prefix=%{buildroot}%{_prefix} --install-lib=%{buildroot}%py_platsitedir

#cp -Rp * %{buildroot}

mkdir -p %{buildroot}%{_bindir}
#icons
mkdir -p %{buildroot}%{_liconsdir}
mkdir -p %{buildroot}%{_iconsdir}
mkdir -p %{buildroot}%{_miconsdir}
cp data/icones/%{name}-48.png %{buildroot}%{_iconsdir}/%{name}.png
cp data/icones/%{name}-48.png %{buildroot}%{_miconsdir}/%{name}.png
cp data/icones/%{name}-48.png %{buildroot}%{_liconsdir}/%{name}.png
cp data/icones/pymecavideo.svg %{buildroot}%{_iconsdir}/
mkdir %{buildroot}%py_platsitedir/%{name}/help/
cp data/help/* %{buildroot}%py_platsitedir/%{name}/help/

#mkdir -p %{buildroot}%{_datadir}/applications
#cp pymecavideo.desktop %{buildroot}%{_datadir}/applications

#help
mkdir -p %{buildroot}/%_docdir/HTML/fr/pymecavideo/
cp -r %{buildroot}%py_platsitedir/%{name}/help/*.png %{buildroot}/%_docdir/HTML/fr/pymecavideo/
cp -r %{buildroot}%py_platsitedir/%{name}/help/*.css %{buildroot}/%_docdir/HTML/fr/pymecavideo/
cp -r %{buildroot}%py_platsitedir/%{name}/help/help-fr.* %{buildroot}/%_docdir/HTML/fr/pymecavideo/

cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
python %py_platsitedir/pymecavideo/__init__.py
EOF

chmod a+x %{buildroot}%{_bindir}/%{name}
%clean 
rm -rf %{buildroot} 

%files
%{_bindir}/pymecavideo
%{python_sitelib}/%{name}*
#%{_datadir}/applications/%{name}.desktop 
%{_datadir}/icons/%{name}.*
%{_datadir}/icons/*/%{name}.*
%{_docdir}/HTML/fr/%{name}

#%{_libdir}

%defattr(-, root, root,755)
