%global	modname	cysignals

# Python files are installed into nonstandard locations
%global _python_bytecompile_extra 0

Name:		python-%{modname}
Version:	1.10.2
Release:	7%{?dist}
Summary:	Interrupt and signal handling for Cython
License:	LGPLv3+
URL:		https://github.com/sagemath/%{modname}
Source0:	https://github.com/sagemath/%{modname}/releases/download/%{version}/%{modname}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	pari-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1445411#c2
Patch0:		%{name}-gdb.patch
# Linux already clears the FPU state
Patch1:		%{name}-emms.patch
# Counteract _FORTIFY_SOURCE
Patch2:		%{name}-fortify.patch
# Fix underlinked signals.so
Patch3:		%{name}-underlink.patch
# Do not fail if cysignals_crash_logs cannot be created
Patch4:		%{name}-crash-logs.patch
# Remove workaround for Cython bug that is already fixed in Fedora
Patch5:		%{name}-sigismember.patch

%global _description %{expand:
When writing Cython code, special care must be taken to ensure that the
code can be interrupted with CTRL-C. Since Cython optimizes for speed,
Cython normally does not check for interrupts. For example, code like
the following cannot be interrupted in Cython:

while True:
    pass

The cysignals package provides mechanisms to handle interrupts
(and other signals and errors) in Cython code.

See http://cysignals.readthedocs.org/ for the full documentation.}

%description	%{_description}

%package	-n python3-%{modname}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:	python3-devel
BuildRequires:	python3-docs
BuildRequires:	python3dist(cython)
BuildRequires:	python3dist(setuptools)

%description	-n python3-%{modname} %{_description}

%package	-n python3-%{modname}-devel
Summary:	%{summary} headers files
%{?python_provide:%python_provide python3-%{modname}-devel}
Requires:	python3-%{modname}

%description	-n python3-%{modname}-devel %{_description}

%package	doc
Summary:	Documentation for %{name}
BuildRequires:	python3dist(sphinx)
Requires:	python3-%{modname}
BuildArch:	noarch
%description	doc
Documentation and examples for %{name}.

%prep
%autosetup -p0 -n %{modname}-%{version}

# Use local objects.inv for intersphinx
sed -i "s|'https://docs\.python\.org/2\.7', None|'https://docs.python.org/3', '%{_docdir}/python3-docs/html/objects.inv'|" docs/source/conf.py

# Build for python 3
sed -i 's/language_level=2/language_level=3/' setup.py

%build
%configure
%py3_build

# Build the documentation
export PYTHONPATH=$PWD/$(ls -1d build/lib.linux*%{python3_version})
%__make -C docs html
rst2html --no-datestamp README.rst README.html

%install
%py3_install
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -farp docs/build/html %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_docdir}/%{name}/html/.buildinfo

%check
PATH=%{buildroot}%{_bindir}:$PATH
PYTHONPATH=%{buildroot}%{python3_sitearch}
export PATH PYTHONPATH
%{__python3} rundoctests.py src/cysignals/*.pyx

%files		-n python3-%{modname}
%license LICENSE
%doc README.html
%{_bindir}/%{modname}-CSI
%{_datadir}/%{modname}/
%{python3_sitearch}/%{modname}
%{python3_sitearch}/%{modname}-*.egg-info
%exclude %{python3_sitearch}/%{modname}/*.h
%exclude %{python3_sitearch}/%{modname}/*.pxd
%exclude %{python3_sitearch}/%{modname}/*.pxi

%files		-n python3-%{modname}-devel
%{python3_sitearch}/%{modname}/*.h
%{python3_sitearch}/%{modname}/*.pxd
%{python3_sitearch}/%{modname}/*.pxi

%files		doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Jerry James <loganjerry@gmail.com> - 1.10.2-5
- Do not try to write to an unwritable directory (bz 1751021)
- Fix cross-references in the documentation

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Jerry James <loganjerry@gmail.com> - 1.10.2-1
- New upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Jerry James <loganjerry@gmail.com> - 1.8.1-1
- New upstream release
- Drop python2 subpackages (bz 1663842)

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.7.2-1
- New upstream release (bz 1601237)
- Drop upstreamed -import patch
- The Cython libraries are used at runtime, so add Requires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-2
- Rebuilt for Python 3.7

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.7.1-1
- New upstream version for sagemath 8.2 (bz 1473458)
- Add -fortify, -import, and -underlink patches

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.4-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 08 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.2-1
- Update to version required by sagemath 8.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 27 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.2-3
- Correct mixed tabs and spaces in the spec (#1445411#c5)

* Wed Apr 26 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.2-2
- Remove python preloading (#1445411#c2)
- Add python provides to python3 subpackage (#1445411#c3)
- Add changelog section (#1445411#c3)
- Add URL tag (#1445411#c3)
- Correct license to LGPLv3+ (#1445411#c3)
- Change doc subpackage to noarch
- Correct owner of documentation directory (#1445411#c3)
- Do not call the emms instruction on x86 (#1445411#c3)
- Do not install .buildinfo file in doc subpackage (#1445411#c3)
- Correct problems in python3 tests in %%check due to Popen python
- Install a python 2 or 3 specific cysignals-CSI
- Add requires to the LICENSE file in the doc subpackage (#1445411#c3)

* Wed Apr 26 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.2-1
- Initial python-cysignals spec.
