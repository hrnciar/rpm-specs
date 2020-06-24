%{?python_enable_dependency_generator}

%global modname javabridge
%global commit0 c7ccaed43ac7752c4ca361abb04fcb4e9ebdb069
%global date0   20190729
%global scommit0 %(c=%{commit0}; echo ${c:0:7})


Name:           python-%{modname}
Version:        1.0.18
Release:        5.%{date0}git%{scommit0}%{?dist}
Summary:        Python wrapper for the Java Native Interface

License:        MIT
URL:            https://github.com/LeeKamentsky/python-%{modname}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
Patch0:         %{modname}-rhino-noversion.patch
#Patch1:         %%{modname}-cython-level3.patch

%global _description\
The javabridge Python package makes it easy to start a Java virtual machine (JVM)\
from Python and interact with it. Python code can interact with the JVM using a\
low-level API or a more convenient high-level API.

%description
%_description
An python module which provides a convenient example.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
BuildRequires:  java-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  gcc
BuildRequires:  rhino
Requires:       rhino
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

# https://github.com/LeeKamentsky/python-javabridge/issues/170
ExclusiveArch:  i686 x86_64

%description -n python%{python3_pkgversion}-%{modname}
%_description

%prep
%autosetup -p1 -npython-%{modname}-%{commit0}
# unbundle
find . -name \*.jar -print -delete
ln -s %{_javadir}/rhino.jar %{modname}/jars

%build
%py3_build
%{__python3} setup.py build_sphinx
find docs/_build -name .\* -print -delete

%install
%py3_install

%check
export PYTHONPATH=tests-install:%{buildroot}%{python3_sitelib}
%{__python3} setup.py develop --install-dir=tests-install
%{__python3} setup.py nosetests

# Note that there is no %%files section for the unversioned python module
%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE
%doc README.rst
%doc docs/_build/html
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.18-5.20190729gitc7ccaed
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-4.20190729gitc7ccaed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 1.0.18-3.20190729gitc7ccaed
* use new snapshot
- exclusive x86

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 1.0.18-2.20190723git16d6c91
- use latest git snapshot to support cython with python3

* Sat May 11 2019 Raphael Groner <projects.rg@smart.ms> - 1.0.18-1
- initial
