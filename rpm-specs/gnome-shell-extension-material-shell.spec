%global uuid material-shell@papyelgringo

Name: gnome-shell-extension-material-shell
Version: 8
Release: 1%{?dist}
Summary: Modern desktop interface for Linux
BuildArch: noarch

License: MIT
URL: https://github.com/PapyElGringo/material-shell
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Requires: gnome-shell >= 3.34.0

%description
A modern desktop interface for Linux extending GNOME Shell.

Providing an unique, simple, productivity oriented, innovative and automated
mouse and keyboard workflow which aims to be faster and easier to use and
creates a great user experience.

Powered by its unique spatial model, its modern material design interface, its
tiling engine and its persistability.

How to install:

1. Reload gnome-shell by logout and re-login
2. Open 'gnome-extensions-app' and activate 'Material-shell' extension

or run in terminal:

  gnome-extensions enable %uuid


%prep
%autosetup -n material-shell-%{version} -p1


%install
rm -rf documentation/ \
    Makefile
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -ap * %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

pushd %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
rm  CONTRIBUTING.md \
    README.md \
    LICENSE
popd


%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Fri Oct 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 8-1
- build(update): 8

* Mon Sep 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 7-1
- Update to 7

* Sat Sep 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 6-1
- Update to 6

* Tue Sep 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 5-1
- Update to 5

* Wed Sep 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 4-1
- Update to 4

* Mon Aug 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3-2
- Bump minimum required gnome-shell version

* Mon Aug 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3-1
- Update to 3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-2.20200610git7d366e1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1-1.20200610git7d366e1
- Update to '2-beta'

* Wed Mar 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1-1.20200311gitd9fa515
- Update to latest git snapshot

* Mon Mar 09 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.10.20200309gitafc618b
- Update to latest git snapshot

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20200103git689c32e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.9.20200103git689c32e
- Update to latest git snapshot

* Tue Dec 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.9.20191210gitbeb5c15
- Update to latest git snapshot

* Mon Oct 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.9.20191016gite7017db
- Update to latest git snapshot

* Wed Sep 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.8.20190904git9b4e16d
- Update to latest git snapshot

* Fri Jul 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.7.20190720git2aad584
- Update to latest git snapshot

* Wed Jul 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.6.20190717gitac433ba
- Update to latest git snapshot

* Sun Jul 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20190706git96e68b8
- Initial package
- Thanks to Robert-André Mauchin <zebob.m@gmail.com> for help with packaging (as always) and review
