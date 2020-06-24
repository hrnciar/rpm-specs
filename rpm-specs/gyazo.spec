%global upstream_name Gyazo-for-Linux

Name: gyazo
Version: 1.2
Release: 11%{?dist}
Summary: Screen capture (screenshot) tool
License: GPLv3+
BuildArch: noarch
URL: https://gyazo.com/
Source0: https://github.com/gyazo/Gyazo-for-Linux/archive/1.2.tar.gz
Source1: gyazo.1
Patch0: fix_desktop_version.patch
Requires: ruby rubygems rubygem(json)
Requires: %{_bindir}/ps
Requires: ImageMagick
Requires: xorg-x11-utils
BuildRequires: desktop-file-utils

%description
Seriously Instant Screen-Grabbing (screenshot) Gyazo
lets you instantly grab  the screen and upload the image to the web. 
You can easily share them on Chat, Twitter, Blog, Tumblr, etc.

%prep
%setup -q -n %{upstream_name}-%{version}
%patch0
%build
%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/pixmaps
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/ruby/%{name}
mkdir -p %{buildroot}/%{_mandir}/man1
cp %{SOURCE1} %{buildroot}/%{_mandir}/man1/%{name}.1
cp src/%{name}.rb %{buildroot}/%{_datadir}/ruby/%{name}
cp src/%{name}.desktop %{buildroot}/%{_datadir}/applications
cp icons/%{name}.png %{buildroot}/%{_datadir}/pixmaps
ln -f -s %{_datadir}/ruby/%{name}/%{name}.rb %{buildroot}/%{_bindir}/%{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%attr(755,root,root) %{_bindir}/%{name}
%doc README.md
%license debian/copyright
%{_datadir}/ruby/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Added word screenshot to description and summary to make it more easily foundable

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 26 2017 Vít Ondruch <vondruch@redhat.com> - 1.2-5
- Add missing dependencies.

* Thu Oct 26 2017 Vít Ondruch <vondruch@redhat.com> - 1.2-4
- Drop the explicit dependency on rubypick.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Patrik Opravil <patrikopravil@gmail.com> - 1.2-1
- Used this spec file as template
- Used Source https://github.com/gyazo/Gyazo-for-Linux/archive/1.2.tar.gz
- Built as noarch
- Made link in install section insted of post
- Added documentation, licence and manpage to files
- Added and Patched desktopfile
- Added requires
- Made manpage
- Edited install section
- Added check section
- Edited rights to links

* Mon Jul 13 2015 Yosuke Tamura <yosuke.tamura.tp8@gmail.com>
- Added this SPEC file to build RPM package.

