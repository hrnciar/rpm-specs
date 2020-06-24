%global srcname pytest-arraydiff
%global sum The py.test arraydiff plugin

Name:           python-%{srcname}
Version:        0.3
Release:        6%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

%description
This is a py.test plugin to facilitate the generation and comparison of
data arrays produced during tests.

The basic idea is that you can write a test that generates a Numpy array
(or other related objects depending on the format). You can then either
run the tests in a mode to generate reference files from the arrays, or
you can run the tests in comparison mode, which will compare the results
of the tests to the reference ones within some tolerance.

At the moment, the supported file formats for the reference files are:
* A plain text-based format (baed on Numpy loadtxt output)
* The FITS format (requires astropy). With this format, tests can return
  either a Numpy array for a FITS HDU object.



%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       python3-numpy
Requires:       python3-pytest
Requires:       python3-six
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This is a py.test plugin to facilitate the generation and comparison of
data arrays produced during tests.

The basic idea is that you can write a test that generates a Numpy array
(or other related objects depending on the format). You can then either
run the tests in a mode to generate reference files from the arrays, or
you can run the tests in comparison mode, which will compare the results
of the tests to the reference ones within some tolerance.

At the moment, the supported file formats for the reference files are:
* A plain text-based format (baed on Numpy loadtxt output)
* The FITS format (requires astropy). With this format, tests can return
  either a Numpy array for a FITS HDU object.


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python3-%{srcname}
%license LICENSE
%doc CHANGES.md README.rst
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.3-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2-2
- Rebuilt for Python 3.7

* Sat Mar 17 2018 Christian Dersch <lupinix@mailbox.org> - 0.2-1
- initial packaging effort

