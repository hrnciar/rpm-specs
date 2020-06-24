%global modname grako
%global modfirst %(c=%{modname}; echo ${c:0:1})

Name:           python-%{modname}
Version:        3.18.1
Release:        13%{?dist}
Summary:        Python grammar compiler, EBNF input, PEG/Packrat parser output

License:        BSD
URL:            https://pypi.python.org/pypi/%{modname}/
Source0:        https://pypi.io/packages/source/%{modfirst}/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# needed for tests:
BuildRequires:  python%{python3_pkgversion}-pytest

%description
Grako (for "grammar compiler") takes a grammar in a variation of EBNF
as input, and outputs a memoizing PEG/Packrat parser in Python.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-pygraphviz
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

%description -n python%{python3_pkgversion}-%{modname}
Grako (for "grammar compiler") takes a grammar in a variation of EBNF
as input, and outputs a memoizing PEG/Packrat parser in Python.


%prep
%setup -q -n %{modname}-%{version}

# Edit Makefiles to invoke python3 explicitly, rather than just python.
# This ensures that we run the tests using the python3 interpreter.
find . -name Makefile -exec sed -i 's/python[ \t]/python3 /g' {} +

# Fix Python shebang lines
find -type f -exec sed -i '1s=^#!/usr\(/env\|/bin\)* python[23]\?=#!/usr/bin/python3=' {} +

# Don't package examples/antlr2grako/.ropeproject 
rm -rf examples/antlr2grako/.ropeproject


%build
%py3_build


%install
%py3_install
# install loses the executable permission on bootstrap.py, so fix
chmod a+x %{buildroot}%{python3_sitelib}/%{modname}/bootstrap.py


%check
# make directory needed for bootstrap test
mkdir tmp
make test

# Examples are packaged as documentation, not intended to run in place
# from the doc dir, so they should not be prebuilt. After check, clean
# and remove bytecode.
for e in antlr2grako calc regex
do
  pushd examples/$e
  make clean
  rm -rf __pycache__ */__pycache__
  popd
done


%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE.txt
%doc DESCRIPTION.rst README.md
%doc examples
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.18.1-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.18.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.18.1-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.18.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 3.18.1-2
- Rebuild for Python 3.6

* Fri Dec 16 2016 Eric Smith <brouhaha@fedoraproject.org> 3.18.1-1
- Updated to latest upstream.
- Use find and sed to replace shebang lines in python scripts based on
  http://python-rpm-porting.readthedocs.io/en/latest/applications.html#fixing-shebangs
- Use find and sed to change "python" in Makefiles to "python3".

* Wed Dec 14 2016 Eric Smith <brouhaha@fedoraproject.org> 3.18.0-4
- Moved check section to follow install section in spec.
- Use pushd/popd rather than cd in check section.

* Tue Dec 13 2016 Eric Smith <brouhaha@fedoraproject.org> 3.18.0-3
- Fix dependency on python3-pygraphviz, and move into subpackage.
- Fix shebang lines of examples.
- Clean examples after check.

* Mon Dec 12 2016 Eric Smith <brouhaha@fedoraproject.org> 3.18.0-2
- Add dependency on python3-pygraphviz per package review.
- Add a "mkdir tmp" so diagram test passes.
- Added examples directory as doc.

* Sat Dec 10 2016 Eric Smith <brouhaha@fedoraproject.org> 3.18.0-1
- Updated to latest upstream
- Changes per package review (#1401276).

* Sun Dec 04 2016 Eric Smith <brouhaha@fedoraproject.org> 3.17.0-1
- Initial version.
