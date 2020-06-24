Name:           remake
Version:        0.14
Release:        1%{?dist}
Summary:        Build system that bridges the gap between make and redo

License:        GPLv3+
URL:            https://github.com/silene/%{name}
Source0:        https://github.com/silene/%{name}/archive/%{name}-%{version}.tar.gz
# Find out which test is hanging
Patch0:         %{name}-test.patch

BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  inotify-tools
BuildRequires:  tex-epstopdf
BuildRequires:  urw-base35-fonts

%description
Remake is a build system with features of both make and redo.  See the
documentation for details on usage and control file syntax.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
Provides:       bundled(jquery)

%description doc
Documentation for using and developing %{name}.

%prep
%autosetup -p0 -n %{name}-%{name}-%{version}

%build
g++ $RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -o remake remake.cpp \
    $RPM_LD_FLAGS
doxygen

%install
# Install the binary
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 remake %{buildroot}%{_bindir}

# Install the doxygen documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a doxydoc/html %{buildroot}%{_docdir}/%{name}

%check
cd testsuite
./all.sh

%files
%doc README.md
%exclude  %{_docdir}/%{name}/html
%{_bindir}/%{name}

%files doc
%doc %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/README.md

%changelog
* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 0.14-1
- Version 0.14

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.12-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Nov  7 2014 Jerry James <loganjerry@gmail.com> - 0.12-1
- New upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan  6 2014 Jerry James <loganjerry@gmail.com> - 0.11-1
- New upstream release
- Add inotify-tools BR for new tests

* Tue Jul 30 2013 Jerry James <loganjerry@gmail.com> - 0.9-1
- New upstream release
- More BRs for the documentation
- Adapt to Rawhide _docdir change

* Fri Jun 14 2013 Jerry James <loganjerry@gmail.com> - 0.8-1
- New upstream release
- BR doxygen-latex instead of just doxygen

* Mon Jun  3 2013 Jerry James <loganjerry@gmail.com> - 0.7-1
- New upstream release

* Tue May 28 2013 Jerry James <loganjerry@gmail.com> - 0.5-1
- New upstream release

* Wed Apr 17 2013 Jerry James <loganjerry@gmail.com> - 0.4-3
- Use a tagged tarball instead of one derived from a git commit
- Split documentation out into a subpackage

* Tue Apr 16 2013 Jerry James <loganjerry@gmail.com> - 0.4-2
- Ship doxygen documentation

* Mon Apr  8 2013 Jerry James <loganjerry@gmail.com> - 0.4-1
- Initial RPM
