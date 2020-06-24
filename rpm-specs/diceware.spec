Name:		diceware
Version:	0.9.5
Release:	7%{?dist}
Summary:	Create passphrases which one can remember

License:	GPLv3+
URL:		https://pypi.python.org/pypi/diceware
Source0:	https://files.pythonhosted.org/packages/source/d/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-runner
BuildRequires:	%{_bindir}/rst2man

%description
A simple command line tool which can create simple passphrases
which human can remember.

%package doc
Summary:    Documentation for Diceware
BuildArch:  noarch
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme
%description doc
Diceware is a simple command line tool which can create simple
passphrases which human can remember.

This package provides documentation for Diceware.



%prep
%autosetup


%build
%py3_build


%install
%py3_install
mkdir -p %{buildroot}%{_mandir}/man1
rst2man docs/manpage.rst %{buildroot}%{_mandir}/man1/diceware.1

pushd docs
PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build-3 -b html -d _build/doctrees . _build/html
popd

# Remove unneeded build artifacts.
rm -rf docs/_build/.buildinfo
rm -rf docs/_build/html/.buildinfo
rm -rf docs/_build/.doctrees


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version}

%files doc
%doc docs/_build/html

%files
%doc README.rst COPYRIGHT
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}*
%{_mandir}/man1/diceware.1*



%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Kushal Das <kushal@fedoraproject.org> - 0.9.5-1
- Updates to 0.9.5 release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 27 2017 Kushal Das <kushal@fedoraproject.org> - 0.9.3-3
- Updates based on review and docs subpackage

* Wed Dec 27 2017 Kushal Das <kushal@fedoraproject.org> - 0.9.3-2
- Updates based on review

* Mon Nov 20 2017 Kushal Das <kushal@fedoraproject.org> - 0.9.3-1
- Initial build
