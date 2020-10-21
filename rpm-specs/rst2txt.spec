%global pypi_name rst2txt

Name:           %{pypi_name}
Version:        1.1.0
Release:        10%{?dist}
Summary:        Convert reStructuredText to plain text

License:        BSD
URL:            https://github.com/stephenfin/rst2txt
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  python3-pytest

%description
reStructuredText is pretty-damn consumable in its raw form, but extensive use
of directives and roles can hamper things or leave the document incomplete in
its raw form.

rst2txt allows you to work around this by evaluating the reStructuredText
source and stripping it of most of its formatting. The end result is a
document that's more readable and has elements that don't make sense in
a plain text document, such as images, stripped.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e 's/use_scm_version=True,/version="%{version}",/g' setup.py

%build
%py3_build

%install
%py3_install
    
%check
PYTHONPATH=%{buildroot}/%{python3_sitelib}/ pytest-%{python3_version} -v tests

%files
%doc README.rst
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-9
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-6
- Update source URL

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-2
- Run tests (rhbz#1714195)

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora
