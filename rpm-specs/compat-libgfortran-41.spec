%define DATE 20071221
%define _unpackaged_files_terminate_build 0
Summary: Compatibility Fortran 95 runtime library version 4.1.2
Name: compat-libgfortran-41
Version: 4.1.2
Release: 57%{?dist}
# libgfortran has an exception which allows
# linking it into any kind of programs or shared libraries without
# restrictions.
License: GPLv2+ with exceptions
Source0: libgfortran-%{version}-%{DATE}.tar.bz2
URL: http://gcc.gnu.org
BuildRequires: gcc-gfortran >= 4.1.2, gettext, bison, flex, texinfo
Patch1: libgfortran41-gthr.patch

%description
This package includes a Fortran 95 runtime library for compatibility
with GCC 4.1.x-RH compiled Fortran applications.

%prep
%setup -q -n libgfortran-%{version}-%{DATE}
%patch1 -p0 -b .gthr~

# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
cp /usr/lib/rpm/config.* .

%build
mkdir obj
cd obj
CFLAGS="$RPM_OPT_FLAGS" FCFLAGS="$RPM_OPT_FLAGS" ../libgfortran/configure --prefix=%{_prefix} --disable-multilib
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd obj
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -m 755 .libs/libgfortran.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/
ln -sf libgfortran.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/libgfortran.so.1

%ldconfig_scriptlets

%files
%{_libdir}/libgfortran.so.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.1.2-48
- Add dist-tag (RHBZ #1237157).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 4.1.2-45
- Update config.guess/sub for new arches

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 21 2007 Jakub Jelinek  <jakub@redhat.com> 4.1.2-36
- new compat library
