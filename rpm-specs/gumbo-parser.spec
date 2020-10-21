Name:           gumbo-parser
Epoch:          1
Version:        0.10.1
Release:        19%{?dist}
Summary:        A HTML5 parser

License:        ASL 2.0
URL:            https://github.com/google/gumbo-parser

Source0:        https://github.com/google/gumbo-parser/archive/v0.10.1.tar.gz#/gumbo-parser-0.10.1.tar.gz
# Fix up Doxyfile
Patch1:         0001-Doxygen-tweaks.patch
# Autotool generated sources
Patch2:         0002-Autotool-generated-sources.patch

# For the tests
BuildRequires:  gcc-c++
BuildRequires: gtest-devel

# For the docs
BuildRequires: doxygen

# For the python bindings
BuildRequires: python3-setuptools
BuildRequires: python3-devel

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented as
a pure C99 library with no outside dependencies. It's designed to serve
as a building block for other tools and libraries such as linters,
validators, templating languages, and refactoring and analysis tools.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	python
Summary:        Python bindings to %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildArch:      noarch

%description	python
Python bindings to %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1

# Package has autotools compatibility issues
# Use prebuilt autotool generated sources
%patch2 -p1
# Fix up permissions
chmod +x config.guess config.sub configure \
depcomp install-sh missing test-driver
# Fix up timestamps
touch -r aclocal.m4 configure m4/*.m4 Makefile.in

# Update Doxyfile
doxygen -u Doxyfile

## Doxygen standard footers are not multilib-compliant
## Create a custom one.
touch footer.html
doxygen -w html /dev/null footer.html /dev/null Doxyfile
sed -i -e 's,\$generatedby,Generated on $date for $projectname by,' footer.html


# Propagate the version number into setup.py
# to fix egg version number
sed -i -e 's,{{VERSION}},%version,' setup.py

%build
%configure --disable-static --disable-silent-rules --docdir=%{_pkgdocdir}
make %{?_smp_mflags}

# Build doxgen docs
doxygen Doxyfile

# python bindings
%{__python3} setup.py build

%check
make check

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

install -m 755 -d ${RPM_BUILD_ROOT}%{_mandir}/man3
install -m 644 docs/man/man3/*.3 ${RPM_BUILD_ROOT}%{_mandir}/man3

install -m 755 -d ${RPM_BUILD_ROOT}%{_pkgdocdir}
cp -r docs/html ${RPM_BUILD_ROOT}%{_pkgdocdir}
install -m 644 {COPYING,*.md} ${RPM_BUILD_ROOT}%{_pkgdocdir}

# python bindings
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%ldconfig_scriptlets


%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/html
%exclude %{_pkgdocdir}/*.md
%{_libdir}/*.so.*

%files devel
%doc %{_pkgdocdir}/html
%doc %{_pkgdocdir}/*.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gumbo.pc
%{_mandir}/man3/*.3*

%files python
%{python3_sitelib}/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.10.1-18
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.10.1-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.10.1-15
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.10.1-11
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:0.10.1-6
- Fix doxygen-1.18.2 incompatibility (F25FTBS, F26FTBFS).

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1:0.10.1-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.10.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 27 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:0.10.1-1
- Update to 0.10.1, bump epoch (RHBZ#1229357).
- Rebase patches.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.20140503git3a61e9a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.20140503git3a61e9a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0-0.5.20140503git3a61e9a
- Update tarball.

* Fri Jun 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0-0.5.20131204git87b99f2
- Own %%{_pkgdocdir}.
- Fix *-python egg version numbering.

* Mon Dec 23 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0-0.2.20131204git87b99f2
- Update tarball.

* Thu Oct 17 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0-0.2.20131001gitd90ea2b
- Update tarball.
- Add autotool genered source-files.
- Fix up doxygen support/Work-around doxygen regressions.
- Reflect review feedback.
- Merge main package docs and *devel-docs into common subdir.
- Enforce python3.

* Fri Aug 16 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0-0.1.20130816git88ee911
- Initial Fedora package.
