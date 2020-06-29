%global srcname partd

Name:           python-%{srcname}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Appendable key-value storage

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Key-value byte store with appendable values: Partd stores key-value pairs. \
Values are raw bytes. We append on old values. Partd excels at shuffling \
operations.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-locket
BuildRequires:  python3-toolz
BuildRequires:  python3-numpy >= 1.9.0
BuildRequires:  python3-pandas >= 0.19.0
BuildRequires:  python3-zmq
BuildRequires:  python3-blosc

Requires:    python3-locket
Requires:    python3-toolz
Recommends:  python3-numpy >= 1.9.0
Recommends:  python3-pandas >= 0.19.0
Recommends:  python3-zmq
Recommends:  python3-blosc

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    py.test-%{python3_version}


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Thu Mar 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.10-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.9-1
- Update to latest version

* Mon Sep 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.8-6
- Remove Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.8-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.3.8-2
- Standardize spec a bit more.
- Simplify description a bit.

* Mon Jun 5 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.3.8-1
- New upstream release.

* Sun Feb 26 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.3.7-2
- Add missing dependencies.

* Sun Feb 26 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.3.7-1
- Initial package release.
