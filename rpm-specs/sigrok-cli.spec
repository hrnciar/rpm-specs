Name:           sigrok-cli
Version:        0.7.1
Release:        3%{?dist}
Summary:        Basic hardware access drivers for logic analyzers
License:        GPLv3+
URL:            http://www.sigrok.org
Source0:        %{url}/download/source/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
# libsigrok+decode minor versions have a significantly different API
BuildRequires:  pkgconfig(libsigrok)       >= 0.5.0
BuildRequires:  pkgconfig(libsigrokdecode) >= 0.5.0

%description
%{name} is a command-line tool written in C, which uses both libsigrok and
libsigrokdecode to provide the basic sigrok functionality from the
command-line. Among other things, it's useful for scripting purposes.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%doc NEWS README
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/applications/org.sigrok.%{name}.desktop
%{_datadir}/icons/*/*/*/%{name}.svg

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Dan Horák <dan[at]danny.cz> - 0.7.1-1
- Update to sigrok-cli 0.7.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.7.0-1
- Update to sigrok-cli 0.7.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 11 2016 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.6.0-0
- Update to sigrok-cli 0.6.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Sep 20 2014 Dan Horák <dan[at]danny.cz> - 0.5.0-1
- Update to sigrok-cli 0.5.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Alexandru Gagniuc mr.nuke.me[at]gmail[dot]com - 0.4.0-1
- Update to sigrok-cli 0.4.0

* Mon May 06 2013 Alexandru Gagniuc mr.nuke.me[at]gmail[dot]com - 0.3.1-3
- Drop unused post and postun sections
- Add NEWS README COPYING to doc. (ChangeLog is just a git log, exclude it)
- Don't abuse wildcards (man*/* -> man1/%%{name}.1*)

* Sun May 05 2013 Alexandru Gagniuc mr.nuke.me[at]gmail[dot]com - 0.3.1-2
- Limit libsigrok+decode max version due to incompatible APIs

* Wed Oct 10 2012 Alexandru Gagniuc mr.nuke.me[at]gmail[dot]com - 0.3.1-1
- Initial RPM release
