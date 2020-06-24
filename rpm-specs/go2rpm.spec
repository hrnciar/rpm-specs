Name:           go2rpm
Version:        1
Release:        8%{?dist}
Summary:        Convert Go packages to RPM

License:        MIT
URL:            https://pagure.io/GoSIG/go2rpm
Source0:        https://pagure.io/GoSIG/go2rpm/archive/v%{version}/go2rpm-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       askalono-cli
Requires:       compiler(go-compiler)
%{?python_enable_dependency_generator}

%description
Convert Go packages to RPM.

%prep
%autosetup -n go2rpm-v%{version} -p1

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{_bindir}/go2rpm
%{python3_sitelib}/go2rpm-*.egg-info/
%{python3_sitelib}/go2rpm/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1-8
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1-5
- Rebuilt for Python 3.8

* Sun Aug 04 22:04:10 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1-4
- Replace go-rpm-macros with compiler(go-compiler)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 22:04:32 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1-2
- Add go-rpm-macros require

* Thu Jul 11 18:00:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1-1
- Initial package
