Name:       fapg
Version:    0.43
Release:    2%{?dist}
License:    GPLv2+
Summary:    Fast Audio Playlist Generator
URL:        http://royale.zerezo.com/fapg/
Source:     http://royale.zerezo.com/fapg/%{name}-%{version}.tar.gz
BuildRequires: uriparser-devel
BuildRequires: gcc

%description
FAPG means Fast Audio Playlist Generator.
It is a tool to generate list of audio files (Wav, MP3, Ogg, etc)
in various formats (M3U, PLS, HTML, etc).
It is very useful if you have a large amount of audio files 
and you want to quickly and frequently build a playlist.

It is coded in C to be as fast as possible, and does not use 
any specific audio library (like ID3Lib).
This allow you to deploy it faster and easier, and to have 
better performances since the less informations are loaded.
In the other hand, this tool is not (yet) compatible with 
all the known formats.

%prep
%autosetup

%build
%configure
%make_build

%check
make check

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 29 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.43-1
- Update to 0.43 fixes rhbz#1818114

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.42-6
- added gcc as BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 21 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.42-1
- Rebuilt for new upstream release 0.42
- Removed patch merged upstream
- Spec clean up

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  9 2014 Michael Schwendt <mschwendt@fedoraproject.org> - 0.41-8
- Patch for "-Werror=format-security" build (#1037058).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 02 2008 Paulo Roma <roma@lcg.ufrj.br> 0.41-2
- Fixed license.

* Sat May 17 2008 Paulo Roma <roma@lcg.ufrj.br> 0.41-1
- First spec file.
