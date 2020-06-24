%global commit      7d366e19dc2640a2f9eaadcef410e96a61708783
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20200610

%global uuid    material-shell@papyelgringo

Name:           gnome-shell-extension-material-shell
Version:        1
Release:        1.%{date}git%{shortcommit}%{?dist}
Summary:        Performant and simple opinionated mouse/keyboard workflow

License:        MIT
URL:            https://github.com/PapyElGringo/material-shell
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
BuildArch:      noarch

Requires:       gnome-shell >= 3.32.0

%description
New shell for Gnome following the Material-design guidelines. Proposing a
performant and simple opinionated mouse/keyboard workflow to increase daily
productivity and comfort.

How to install:

1. Reload gnome-shell by logout and re-login
2. Open 'gnome-tweaks' and activate 'Material-shell' extension

or run in terminal:

  gnome-extensions enable %uuid


%prep
%autosetup -n material-shell-%{commit}


%install
rm demo.gif
mkdir -p    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -ap *    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
pushd       %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
rm  LICENSE         \
    README.md       \
    CONTRIBUTING.md
popd


%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
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
