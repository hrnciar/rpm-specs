Name:           saclib
Version:        2.2.7
Release:        5%{?dist}
Summary:        Computer algebra library

License:        MIT
URL:            https://www.usna.edu/Users/cs/wcbrown/qepcad/B/QEPCAD.html
Source0:        https://www.usna.edu/Users/cs/wcbrown/qepcad/INSTALL/%{name}%{version}.tar.gz
# The sources include system-dependent definitions.  The Linux versions support
# only x86 and x86_64.  These versions should work on any Linux system.
Source1:        GC.c
Source2:        sysdep.h
# Add function prototypes and attributes for better optimization. Upstream:
# 20 Nov 2013.
Patch0:         %{name}-attr.patch

BuildRequires:  gcc
BuildRequires:  tex(latex)

%global major %(cut -d. -f1 <<< %{version})

%description
SACLIB is a library of C programs for computer algebra derived from the
SAC2 system.  Hoon Hong was the primary author of that earlier system.

%package devel
Summary:        Development files for saclib
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and library links for developing applications that use
saclib.

%prep
%setup -q -n %{name}%{version}
%patch0
cp -p %{SOURCE1} src
cp -p %{SOURCE2} include

# Generate the makefile
saclib=$PWD bin/mkmake

# Build a shared library instead of a static library and link with -lm
sed -e 's/saclib\${EXTENSION}\.a/libsaclib.so/' \
    -e 's/\${RANLIB}.*/& ${OBJS1} ${OBJS2a} ${OBJS2b} ${OBJS3} ${OBJS4} -lm/' \
    -i lib/objo/makefile

%build
export saclib=$PWD
export CC=gcc
export CFLAGS="%{optflags} -frounding-math"
make %{?_smp_mflags} -C lib/objo SACFLAG="$CFLAGS -fPIC" AR=true \
  RANLIB="gcc -shared $CFLAGS $RPM_LD_FLAGS -Wl,-h,libsaclib.so.%{major} -o"

# Build the documentation
cd doc/user_guide
pdflatex saclocal
pdflatex sackwic
pdflatex saclib
makeindex saclib
pdflatex saclib
pdflatex saclib

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
install -p -m 0755 lib/libsaclib.so %{buildroot}%{_libdir}/libsaclib.so.%{version}
ln -s libsaclib.so.%{version} %{buildroot}%{_libdir}/libsaclib.so.%{major}
ln -s libsaclib.so.%{major} %{buildroot}%{_libdir}/libsaclib.so

# Install the headers
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -p include/*.h %{buildroot}%{_includedir}/%{name}

%ldconfig_scriptlets

%files
%doc README
%license LICENSE
%{_libdir}/libsaclib.so.*

%files devel
%doc doc/user_guide/*.pdf
%{_includedir}/%{name}/
%{_libdir}/libsaclib.so

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Jerry James <loganjerry@gmail.com> - 2.2.7-1
- New upstream release
- Updated URLs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan  7 2015 Jerry James <loganjerry@gmail.com> - 2.2.6-4
- Update URLs
- Use license macro

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Jerry James <loganjerry@gmail.com> - 2.2.6-1
- New upstream release
- Drop upstreamed patches

* Thu Nov 21 2013 Jerry James <loganjerry@gmail.com> - 2.2.5-1
- Initial RPM
