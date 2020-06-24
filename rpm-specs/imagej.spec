Name:           imagej
Version:        1.50
Release:        9.h%{?dist}
Summary:        Image Processing and Analysis in Java

License:        Public Domain
URL:            http://rsbweb.nih.gov/ij/index.html
Source0:        http://rsbweb.nih.gov/ij/download/src/ij150h-src.zip
Source1:        %{name}.desktop
Source2:        http://rsbweb.nih.gov/ij/macros/macros.zip
Source3:        http://rsb.info.nih.gov/ij/download/linux/unix-script.txt
Source4:        imagej.png

# don't copy .class files 
patch0:         %{name}-%{version}-patch0.patch
# modify imagej.sh for fedora compatibility
patch1:         %{name}-%{version}-patch1.patch
BuildArch:      noarch


BuildRequires:  jpackage-utils
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  ant
BuildRequires:  desktop-file-utils


Requires:       jpackage-utils
# java-devel not java for plugins build
Requires:       java-devel >= 1.6.0

%description
ImageJ is a public domain Java image processing program. It can display,        
edit, analyze a wide variety of image data, including image sequences. Imagej   
can be used for quantitative analysis of engineering and scientific image data.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c -n "%{name}-%{version}" 
# patch build.xml
%patch0 -p0 -b .patch0
# unzip macros.zip
unzip -qq -u %{SOURCE2} 
# erase binary and useless files 
rm -rf macros/.FBC*
rm macros/build.xml
rm -rf __MACOSX
#get and patch unix-script.txt
cp %{SOURCE3} ./imagej.sh
%patch1 -p1 -b .patch1

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
cd source
ant build javadocs
cd ..

%install

# install jar
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p source/ij.jar   \
$RPM_BUILD_ROOT%{_javadir}/%{name}.jar


# install javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp api  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}

# install icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/pixmaps

# install data files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p source/build/about.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}/about.jpg
cp -p source/build/IJ_Props.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/IJ_Props.txt

#install macros
chmod 644 macros/About\ Startup\ Macros 
find ./macros -name \*.txt -type f -exec chmod 644 {} \;
find ./macros -type d -exec chmod 755 {} \;
cp -rp macros $RPM_BUILD_ROOT%{_datadir}/%{name}


#install luts
mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/luts 

# install script
mkdir -p $RPM_BUILD_ROOT%{_bindir}
chmod +x imagej.sh
cp -p imagej.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

# directory for plugins
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
#cp source/plugins/JavaScriptEvaluator.source $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/JavaScriptEvaluator.java

# desktop file
desktop-file-install --vendor=""                     \
       --dir=%{buildroot}%{_datadir}/applications/   \
       %{SOURCE1}

%files
%{_javadir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/imagej.png
%{_bindir}/%{name}
%doc source/aREADME.txt source/release-notes.html source/applet.html

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-9.h
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-8.h
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-7.h
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-6.h
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-5.h
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.50-4.h
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-3.h
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-2.h
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 26 2016 Adam Huffman <bloch@verdurin.com> - 1.50-1.h
- Update to upstream release 1.50h

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-8.e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 04 2015 Adam Huffman <bloch@verdurin.com> - 1.48-7.e
- Apply Java docdir fixes from Michael Simacek

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-6.e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 13 2014 Adam Huffman <bloch@verdurin.com> - 1.48-5.e
- Fix bogus dates in changelog

* Wed Aug 13 2014 Adam Huffman <bloch@verdurin.com> - 1.48-4.e
- Fix desktop file to ensure application appears in menus

* Mon Jul 14 2014 Richard Hughes <richard@hughsie.com> - 1.48-3.e
- Ship a larger application icon so the metdata parser can include the app.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-2.e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 26 2013 Adam Huffman <bloch@verdurin.com> - 1.48-1.e
- Update to 1.48e

* Sun Aug 25 2013 Adam Huffman <bloch@verdurin.com> - 1.47-1.v
- Update to 1.47v

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-4.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-3.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-2.d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Adam Huffman <verdurin@fedoraproject.org> - 1.46-1.d
- update to 1.45d

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-2.i
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 30 2010 Georget Fabien <fabien.georget@gmail.com> 1.44-1.i
- update to 1.44i
- create imagej.jar link

* Tue Sep 28 2010 Georget Fabien <fabien.georget@gmail.com> 1.44-1.h
- version 1.44h

* Fri Dec 11 2009 Georget Fabien <fabien.georget@gmail.com> 1.43-1.m
- version 1.43m 

* Sat Nov 21 2009 Georget Fabien <fabien.georget@gmail.com> 1.43-0.5.j
- set build directory to {name}-{version}
- modify wrapper script
- add java-devel to requires

* Sun Nov 15 2009 Georget Fabien <fabien.georget@gmail.com> 1.43-0.4.j
- modify name from ImageJ to imagej
- modify wrapper script for fedora compatibility 

* Tue Nov 10 2009 Georget Fabien <fabien.georget@gmail.com> 1.43-0.3.j
- get macros from  http://rsbweb.nih.gov/ij/macros/macros.zip
- get launch script from  http://rsb.info.nih.gov/ij/download/linux/unix-script.txt
- don't copy macros in the jar but in /usr/share/ImageJ/macros

* Tue Nov 10 2009 Georget Fabien <fabien.georget@gmail.com> 1.43-0.2.j
- change group to Application/Engineering
- change description
- add comments
- change version tag

* Sat Nov 8 2008 Georget Fabien <fabien.georget@gmail.com> 1.43-0.1
- Creation
