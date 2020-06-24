%global srcname tblib

Name:           python-%{srcname}
Version:        1.6.0
Release:        3%{?dist}
Summary:        Traceback serialization library

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch

%global _description \
Traceback serialization library that allows you to: \
  * Pickle tracebacks and raise exceptions with pickled tracebacks in different \
    processes. This allows better error handling when running code over \
    multiple processes (imagine multiprocessing, billiard, futures, celery, \
    etc). \
  * Parse traceback strings and raise with the parsed tracebacks.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-six
BuildRequires:  python3-twisted
BuildRequires:  python3-sphinx >= 1.3
BuildRequires:  python3-sphinx-theme-py3doc-enhanced

Requires:       python3-six

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build

PYTHONPATH="src" \
    sphinx-build-%{python3_version} -E -b html docs build/html


%install
%py3_install


%check
PYTHONPATH="%{buildroot}%{python3_sitelib}:tests" \
    py.test-%{python3_version} -ra tests README.rst


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.0-1
- Update to latest version

* Wed Oct 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-4
- Backport fixes for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.3.2-6
- Drop Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.3.2-2
- Standardize spec a bit more.
- Simplify description a bit.

* Mon Jun 5 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.3.2-1
- New upstream release.

* Mon Feb 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.3.0-1
- Initial package release.
