%global uuid    im.srain.Srain

Name:           srain
Version:        1.1.1
Release:        2%{?dist}
Summary:        Modern, beautiful IRC client written in GTK+ 3

# The entire source code is GPLv3+ except:
# * keypair/        which is BSD
# * sui_side_bar/   which is GPLv2+
License:        GPLv3+ and BSD and GPLv2+
URL:            https://github.com/SrainApp/srain
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(openssl)

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc README.rst
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml
%{_sysconfdir}/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Sun May 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- Update to 1.1.0
- Disable LTO

* Sat Apr 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Sat Mar 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Mon Feb 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-1
- Update to 1.0.0
- Enable LTO

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.6.rc9999
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-0.5.rc9999
- Update to 1.0.0rc9999

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.4.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-0.3.rc5
- Update to 1.0.0rc5

* Mon Apr 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-0.2.rc3
- Initial Package
