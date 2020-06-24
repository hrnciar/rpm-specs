%global major 2.0
%global minor 1

Name:		jaxodraw
Version:	%{major}.%{minor}
Release:	24%{?dist}
Summary:	A Java program for drawing Feynman diagrams
License:	GPLv2+
URL:		http://jaxodraw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{major}-%{minor}_src.tar.gz
# LaTeX file for exporting figures
Source1:	http://downloads.sourceforge.net/%{name}/axodraw4j_2008_11_19.tar.gz
# Desktop file, icon and man page
Source2:	http://downloads.sourceforge.net/%{name}/installer-%{major}-%{minor}.tar.gz
# Wrapper skeleton
Source3:	jaxodraw.sh

BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	desktop-file-utils
# java-devel, we need at least 1.6.0
BuildRequires:	java-devel >= 1:1.6.0
BuildRequires:	jpackage-utils
# Unit testing capabilities
BuildRequires:	ant-junit

Requires:	java >= 1:1.6.0
Requires:	jpackage-utils

%description
JaxoDraw is a Java program for drawing Feynman diagrams. It has a complete
graphical user interface that allows to carry out all actions in a mouse
click-and-drag fashion. Fine-tuning of the diagrams is also possible through
keyboard entries. Graphs may be exported to (encapsulated) postscript and can
be saved in XML files to be used in later sessions.

%package javadoc
Summary:	Javadocs for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%package latex
Summary:	LaTeX style file axodraw4j.sty for documents generated with jaxodraw
License:	LPPL
# In order to compile documents one needs a LaTeX compiler
Requires:	tex(latex)

%description latex
This package contains the LaTeX style file that is needed for EPS export
functionality in jaxodraw.

You need this if you want the export to EPS function to work or if you want to
compile LaTeX files generated with jaxodraw.

%prep
%setup -q -n JaxoDraw-%{major}-%{minor} -a 1 -a 2
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

# Convert documentation encoding
for file in src/doc/{TODO,CHANGELOG,README,BUGS} src/doc/legal/{GNU-,}LICENSE; do
 sed 's/\r//' $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done

# Create invocation script
sed "s|JARFILE|%{_javadir}/%{name}.jar|g" %{SOURCE3} > %{name}
touch -r %{SOURCE3} %{name}

%build
ant jar javadoc

%install
rm -rf %{buildroot}
# Install jar file
install -D -p -m 644 build/%{name}-%{major}-%{minor}.jar %{buildroot}%{_javadir}/%{name}.jar
# Install invocation script
install -D -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}

# Desktop file and icon
desktop-file-install --dir=%{buildroot}%{_datadir}/applications installer-%{major}-%{minor}/OS/Linux/%{name}.desktop
install -D -p -m 644 installer-%{major}-%{minor}/OS/Linux/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
# Man page
install -D -p -m 644 installer-%{major}-%{minor}/OS/Linux/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# LaTeX style
install -D -p -m 644 axodraw4j.sty %{buildroot}%{_datadir}/texmf/tex/latex/axodraw4j/axodraw4j.sty

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: lukas_theussl@users.sf.net
SentUpstream: 2014-05-22
-->
<application>
  <id type="desktop">jaxodraw.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Create and edit Feynman diagrams</summary>
  <description>
    <p>
      Jaxodraw is an application for creating and editing Feynman diagrams,
      with the ability to export to LaTeX.
      Feynman diagrams are a specific diagram scheme to represent the mathematical
      expressions that describe the behavior of subatomic particles.
    </p>
  </description>
  <url type="homepage">http://jaxodraw.sourceforge.net/</url>
  <screenshots>
  <screenshot type="default">http://jaxodraw.sourceforge.net/images/general.png</screenshot>
  </screenshots>
</application>
EOF

%check
# Unit tests fail with Open JDK
#ant test

%post latex -p /usr/bin/texhash
%postun latex -p /usr/bin/texhash

%files
%doc src/doc/* axodraw4j-summary.txt
%{_bindir}/%{name}
%{_javadir}/%{name}.jar
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%files javadoc
%{_javadocdir}/%{name}/

%files latex
%{_datadir}/texmf/tex/latex/axodraw4j/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.0.1-15
- Add an AppData file for the software center

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 29 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-8
- Really respect CLI arguments in shell wrapper.

* Wed Jun 09 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-7
- Respect command line arguments in shell wrapper.

* Mon May 31 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-6
- Switch to using official installer tarball instead of files grabbed from svn.

* Sat May 29 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-5
- Added man page and desktop icon.

* Mon Nov 30 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-4
- Get rid of erroneous Require.

* Fri Oct 23 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-3
- Build and include javadoc.
- Add infrastructure for unit testing.

* Wed Oct 21 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-2
- Generalize requires on latex package from texlive-foo to tex(foo).

* Wed Aug 05 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0.1-1
- Rebase to upstream 2.0-1 which removes the unused license file.

* Wed Jul 29 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0-3
- Branch stylefile into its own package to make licenses clearer.

* Wed Jun 10 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0-2
- Changed license to GPLv2+ (jaxodraw) and LPPL (axodraw4j.sty).

* Sat Jun 06 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 2.0-1
- First release.
