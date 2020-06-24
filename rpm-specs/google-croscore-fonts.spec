BuildArch: noarch

Version:        1.31.0
Release:        8%{?dist}
License:        ASL 2.0
#URL:            

%global foundry           google
%global fontlicense       ASL 2.0
%global fontlicenses      LICENSE-2.0.txt

%global common_description %{expand:
This package contains a collections of fonts that offers improved on-screen
readability characteristics and the pan-European WGL character set and solves
the needs of developers looking for width-compatible fonts to address document
portability across platforms.}

%global fontsummary The width-compatible fonts for improved on-screen readability

%global archivename croscorefonts-%{version}

%global fontfamily1       Arimo
%global fontsummary1      The croscore Arimo family fonts
%global fontpkgheader1    %{expand:
Provides:  google-croscore-arimo-fonts = %{version}-%{release}
Obsoletes: google-croscore-arimo-fonts < %{version}-%{release}
}
%global fonts1            Arimo*.ttf
%global fontconfs1        %{SOURCE1} %{SOURCE4}
%global fontdescription1  %{expand:
%{common_description}

Arimo was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Arial. Arimo offers improved 
on-screen readability characteristics and the pan-European WGL character set 
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.}

%global fontfamily2       Cousine
%global fontsummary2      The croscore Cousine family fonts
%global fontpkgheader2    %{expand:
Provides:  google-croscore-cousine-fonts = %{version}-%{release}
Obsoletes: google-croscore-cousine-fonts < %{version}-%{release}
}
%global fonts2            Cousine*.ttf
%global fontconfs2        %{SOURCE2} %{SOURCE5}
%global fontdescription2  %{expand:
%{common_description}

Cousine was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Courier New. Cousine offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.}

%global fontfamily3       Tinos
%global fontsummary3      The croscore Tinos family fonts
%global fontpkgheader3    %{expand:
Provides:  google-croscore-tinos-fonts = %{version}-%{release}
Obsoletes: google-croscore-tinos-fonts < %{version}-%{release}
}
%global fonts3            Tinos*.ttf
%global fontconfs3        %{SOURCE3} %{SOURCE6}
%global fontdescription3  %{expand:
%{common_description}

Tinos was designed by Steve Matteson as an innovative, refreshing serif design
that is metrically compatible with Times New Roman. Tinos offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to
address document portability across platforms.}


Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/%{archivename}.tar.bz2

Source1:        62-%{fontpkgname1}.conf
Source2:        62-%{fontpkgname2}.conf
Source3:        62-%{fontpkgname3}.conf
Source4:        30-0-%{fontpkgname1}.conf
Source5:        30-0-%{fontpkgname2}.conf
Source6:        30-0-%{fontpkgname3}.conf

# Upstream has not provided license text in their tarball release
# Add ASL2.0 license text in LICENSE-2.0.txt file
Source8:        LICENSE-2.0.txt

Name: google-croscore-fonts
Summary: The width-compatible fonts for improved on-screen readability

%description
%wordwrap -v common_description

%fontpkg -a

%prep
%setup -q -n croscorefonts-%{version}
cp -p %{SOURCE8} .

%build
%fontbuild -a

%install
echo %{fontpkgname}
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Sun May 24 2020 Parag Nemade <pnemade AT redhat DOT com> - 1.31.0-8
- Update fontconfig DTD id in conf file

* Wed Mar 18 2020 Parag Nemade <pnemade AT redhat DOT com> - 1.31.0-7
- Update CI script for new installed font path

* Tue Mar 10 2020 Parag Nemade <pnemade AT redhat DOT com> - 1.31.0-6
- Convert to new fonts packaging guidelines
- Dropped Obsoletes: google-croscore-symbolneu-fonts (Added in F29)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.31.0-2
- Move Obsoletes: to common subpackage

* Mon Nov 12 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.31.0-1
- Update to 1.31.0 version
- Dropped SymbolNeu subpackage as upstream stopped releasing it

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 20 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.23.0-6
- Add metainfo files to show Arimo, Cousine, Tinos fonts in gnome-software

* Wed Sep 03 2014 Parag Nemade <pnemade AT redhat DOT com>- 1.23.0-5
- Drop fontconfig for Symbol Neu font
- Fix rh#1037882 - Wrong character displayed with google-croscore-symbolneu-fonts installed 

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Parag Nemade <pnemade AT redhat DOT com>- 1.23.0-1
- Update to next upstream release 1.23.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Parag Nemade <pnemade AT redhat DOT com>- 1.21.0-3
- Resolves:rh#814631-Typo in 62-google-croscore-cousine-fontconfig.conf

* Tue Mar 27 2012 Parag Nemade <pnemade AT redhat DOT com>- 1.21.0-2
- Updated fontconfig rules.

* Wed Mar 21 2012 Parag Nemade <pnemade AT redhat DOT com>- 1.21.0-1
- Initial packaging
