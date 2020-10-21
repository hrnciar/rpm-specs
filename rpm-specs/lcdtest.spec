Name:           lcdtest
URL:            http://www.brouhaha.com/~eric/software/lcdtest/
Version:        1.18
Release:        25%{?dist}
License:        GPLv3
Summary:        Displays monitor test patterns
Source:         http://www.brouhaha.com/~eric/software/%{name}/download/%{name}-%{version}.tar.gz

Patch0:         0001-RobustFontPath.patch

Requires:       liberation-mono-fonts
Requires:       fontconfig

BuildRequires:  gcc
BuildRequires:  scons >= 1.2.0
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  netpbm-progs
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel

%description
lcdtest is a utility to display LCD monitor test patterns.  It may be
useful for adjusting the pixel clock frequency and phase on LCD
monitors when using analog inputs, and for finding pixels that are
stuck on or off.

%prep
%setup -q
%patch0 -p1

%build
scons %{_smp_mflags} CFLAGS="%{optflags}"

%install
scons %{_smp_mflags} CFLAGS="%{optflags}" \
        --buildroot=%{buildroot} \
        --bindir=%{_bindir} \
        --mandir=%{_mandir} \
        --datadir=%{_datadir} \
        install
mkdir -p %{buildroot}/usr/share/pixmaps
mv %{buildroot}/usr/share/icons/hicolor/scalable/apps/lcdtest.svg \
   %{buildroot}/usr/share/pixmaps
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1.*
%doc COPYING README
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Morian Sonnet <MorianSonnet@googlemail.com> - 1.18-23
- Add patch to automatically determine font path

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.18-12
- Modernize spec.

* Mon Jun 16 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.18-11
- Fix scons syntax (#1105976)
- Update to latest packaging guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 18 2010 Eric Smith <eric@brouhaha.com> 1.18-4
- change require for font from file to package

* Wed Jan 27 2010 Eric Smith <eric@brouhaha.com> 1.18-3
- change the .gz to .* in case the man page compression changesn

* Wed Jan 27 2010 Eric Smith <eric@brouhaha.com> 1.18-2
- move icon to /usr/share/pixmaps, and other minor spec cleanup based on
  package review by Jussi Lehtola

* Tue Jan 26 2010 Eric Smith <eric@brouhaha.com> 1.18-1
- initial version
