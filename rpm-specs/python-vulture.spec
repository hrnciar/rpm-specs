%global module_name vulture
%global common_desc \
Vulture finds unused classes, functions and variables in your code. \
This helps you cleanup and find errors in your programs. If you run it \
on both your library and test suite you can find untested code. \
Due to Python’s dynamic nature, static code analyzers like vulture \
are likely to miss some dead code. Also, code that is only called \
implicitly may be reported as unused. Nonetheless, vulture can be a \
very helpful tool for higher code quality.

Name:		python-%{module_name}
Version:	1.0
Release:	4%{?dist}
Summary:	Find Dead Code

License:	MIT
URL:		https://pypi.python.org/pypi/vulture
Source0:	https://files.pythonhosted.org/packages/source/v/%{module_name}/%{module_name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{common_desc}

%package -n	python3-%{module_name}
Summary:	Find Dead Code
%{?python_provide:%python_provide python3-%{module_name}}

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
# Required by tests
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov

Requires:	python3-setuptools
%description -n	python3-%{module_name}
%{common_desc}

%prep
%autosetup -n	%{module_name}-%{version}
# Remove shebang
sed -i '1{/^#!/d}' vulture/*.py

%build
%py3_build

%install
%py3_install
mv %{buildroot}%{_bindir}/%{module_name} %{buildroot}%{_bindir}/%{module_name}-%{python3_version}

ln -s %{_bindir}/vulture-%{python3_version} %{buildroot}/%{_bindir}/vulture-3
ln -s %{_bindir}/vulture-%{python3_version} %{buildroot}/%{_bindir}/vulture

%check
# Temporary disable tests until vulture is released with fixes for python 3.8
#export PYTHONPATH=.
#py.test-3

%files -n	python3-%{module_name}
%doc README.rst
%license LICENSE.txt
%{_bindir}/%{module_name}
%{_bindir}/%{module_name}-3
%{_bindir}/%{module_name}-%{python3_version}
%{python3_sitelib}/%{module_name}/__pycache__
%{python3_sitelib}/%{module_name}
%{python3_sitelib}/%{module_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Yatin Karel <ykarel@redhat.com> - 1.0-1
- Drop python2 sub package (Resolves #1740990)
- Update to 1.0 (Resolves #1586070)
- Disable tests temporary (Resolves #1716536)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.27-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Yatin Karel <ykarel@redhat.com> - 0.27-2
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Yatin Karel <ykarel@redhat.com> - 0.27-1
- Update to 0.27 (#1586070)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.26-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 0.26-1
- Update to 0.26 (#1485917)

* Wed Aug 16 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 0.25-1
- Update to 0.25 (#1472024)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Yatin Karel <ykarel@redhat.com> - 0.16-1
- Sync with upstream release 0.16

* Wed Jul 05 2017 Yatin Karel <ykarel@redhat.com> - 0.14-3
- Fix Changelog release

* Wed Jul 05 2017 Yatin Karel <ykarel@redhat.com> - 0.14-2
- Use versioned package, python2-setuptools(not python-setuptools)

* Tue Jun 20 2017 Yatin Karel <ykarel@redhat.com> - 0.14-1
- Initial package import

