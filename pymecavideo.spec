%define name	pymecavideo
%define version	5.4
%define release	2
%define title	pymecavideo

Name:		%{name} 
Summary:	Pymecavideo permet de tracer les trajectoires décrites par un  ou plusieurs points d'un objet en utilisant une video
Version:	%{version} 
Release:	%{release} 
Source:		%{name}-%{version}.tar.gz

URL:		http://outilsphysiques.tuxfamily.org/pmwiki.php/Oppl/Pymecavideo
Group:		Sciences/Physics
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	python
Obsoletes:	%{name} < %{version}
BuildArch:	noarch
Requires:	python-qt4
Requires:       ffmpeg
Requires:	vlc

BuildRoot:	%{_tmppath}/%{name}-buildroot 
License:	GPLv3 


%description
pymecavideo permet de tracer point par point la trajectoire de point ainsi que
choisir un référentiel particulier pour étudier la trajectoire dans celui-ci.
Les données ainsi recueillies peuvent être exportées dans un logiciel de
traitement.

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
python setup.py install --prefix=%{buildroot}%{_prefix}

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
%clean 
rm -rf %{buildroot} 

%files
%defattr(-, root, root)
%{_bindir}/pymecavideo
%py_puresitedir/%{name}*
#%{_datadir}/applications/%{name}.desktop 
%{_datadir}/icons/%{name}.*
%{_datadir}/icons/*/%{name}.*
%lang(fr) %{_docdir}/HTML/fr/%{name}


%changelog
* Sat Apr 16 2011 Olivier Faurax <ofaurax@mandriva.org> 5.4-1mdv2011.0
+ Revision: 653864
- New version 5.4

* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 5.2-1mdv2011.0
+ Revision: 599632
- should be noarch package

  + Olivier Faurax <ofaurax@mandriva.org>
    - fix spec for new tar.gz hierarchy
    - New version + cleanup of %%files

* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 4.0-3mdv2011.0
+ Revision: 599386
- correct spec file name
- fix for py2.7

* Sat Nov 20 2010 Olivier Faurax <ofaurax@mandriva.org> 4.0-2mdv2011.0
+ Revision: 599266
- rebuild

* Mon Jan 11 2010 Olivier Faurax <ofaurax@mandriva.org> 4.0-1mdv2011.0
+ Revision: 489996
- import pymecavideo


