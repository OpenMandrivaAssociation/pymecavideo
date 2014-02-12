%define title	pymecavideo

Name:		pymecavideo
Summary:	Tracer les trajectoires décrites par un ou plusieurs points d'un objet
Version:	5.4
Release:	3
Source:		%{name}-%{version}.tar.gz

URL:		http://outilsphysiques.tuxfamily.org/pmwiki.php/Oppl/Pymecavideo
Group:		Sciences/Physics
BuildRequires:	python
BuildArch:	noarch
Requires:	python-qt4
Requires:   ffmpeg
Requires:	vlc
License:	GPLv3 


%description
pymecavideo permet de tracer point par point la trajectoire de point ainsi que
choisir un référentiel particulier pour étudier la trajectoire
dans celui-ci.
Les données ainsi recueillies peuvent être exportées dans un logiciel de
traitement.

%prep 
%setup -q -n %version

%build 
#make
python setup.py build

%install
mkdir -p %{buildroot}%{_prefix}
#mkdir %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}

#python setup.py install --root %{buildroot}
python setup.py install --prefix=%{buildroot}%{_prefix}

mkdir -p %{buildroot}%{_bindir}
#icons
mkdir -p %{buildroot}%{_liconsdir}
mkdir -p %{buildroot}%{_iconsdir}
mkdir -p %{buildroot}%{_miconsdir}
cp data/icones/%{name}-48.png %{buildroot}%{_iconsdir}/%{name}.png
cp data/icones/%{name}-48.png %{buildroot}%{_miconsdir}/%{name}.png
cp data/icones/%{name}-48.png %{buildroot}%{_liconsdir}/%{name}.png
cp data/icones/pymecavideo.svg %{buildroot}%{_iconsdir}/
mkdir %{buildroot}%py_puresitedir/%{name}/help/
cp data/help/* %{buildroot}%py_puresitedir/%{name}/help/

#mkdir -p %{buildroot}%{_datadir}/applications
#cp pymecavideo.desktop %{buildroot}%{_datadir}/applications

#help
mkdir -p %{buildroot}/%_docdir/HTML/fr/pymecavideo/
cp -r %{buildroot}%py_puresitedir/%{name}/help/*.png %{buildroot}/%_docdir/HTML/fr/pymecavideo/
cp -r %{buildroot}%py_puresitedir/%{name}/help/*.css %{buildroot}/%_docdir/HTML/fr/pymecavideo/
cp -r %{buildroot}%py_puresitedir/%{name}/help/help-fr.* %{buildroot}/%_docdir/HTML/fr/pymecavideo/

cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
python %py_puresitedir/pymecavideo/__init__.py
EOF

chmod a+x %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/pymecavideo
%py_puresitedir/%{name}*
#%{_datadir}/applications/%{name}.desktop 
%{_datadir}/icons/%{name}.*
%{_datadir}/icons/*/%{name}.*
%lang(fr) %{_docdir}/HTML/fr/%{name}
