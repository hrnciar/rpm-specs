Name:           porcupine
Version:        0.1.0
Release:        8%{?dist}
Summary:        Web browser to copy URL to clipboard

License:        GPLv3
URL:            https://github.com/micahflee/porcupine
Source0:        https://github.com/micahflee/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-qt5
BuildRequires:  desktop-file-utils
Requires:       python3-qt5


%description
Setting porcupine as a default browser will help you to click on any URL and
get it copied into your clipboard.

%prep
%autosetup


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications \
share/porcupine.desktop

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{python3_sitelib}/%{name}*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Kushal Das <kushal@fedoraproject.org> - 0.1.0-1
- Initial package

