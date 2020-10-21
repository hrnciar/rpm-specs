Name:           fastbit
Version:        2.0.3
Release:        18%{?dist}
Summary:        An Efficient Compressed Bitmap Index Technology
License:        BSD
URL:            https://sdm.lbl.gov/fastbit/
Source0:        https://code.lbl.gov/frs/download.php/file/426/%{name}-%{version}.tar.gz

# Code patch to fix format truncation issue, sent to upstream ML
Patch0:         fastbit_format_truncation.patch

# Code patch to fix FSF address in fbmerge.cpp, sent to upstream ML
Patch1:         fastbit_fsf_address.patch

# Code patch to remove indentation warnings, sent to upstream ML
Patch2:         fastbit_indentation.patch

# Code patch to remove unused variable warnings, sent to upstream ML
Patch3:         fastbit_unused_variable.patch

# Build system patch to ensure linkage to pthread
Patch10:        fastbit_pthread_linkage.patch

# Build system patch for tests to use compiled binaries, not libtool wrappers
Patch11:        fastbit_tests_use_binaries.patch

# Build system patch to avoid versioning the JNI shared library (plugin)
Patch12:        fastbit_jni_avoid_version.patch

# Fedora patch for java bindings to use System.load not System.loadLibrary
Patch20:        fastbit_java_system_load.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  perl-interpreter

ExcludeArch:    s390x

%description
FastBit is an open-source data processing library following the spirit of NoSQL
movement. It offers a set of searching functions supported by compressed bitmap
indexes. It treats user data in the column-oriented manner similar to
well-known database management systems such as Sybase IQ, MonetDB, and Vertica.
It is designed to accelerate user's data selection tasks without imposing undue
requirements.

%package devel
Summary: FastBit development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development package for FastBit.  Includes headers, libraries and man pages for
using FastBit API.

%package java
Summary: FastBit Java libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description java
FastBit API bindings for java using JNI.

%prep
%autosetup -p1 -n %{name}-%{version}

# remove bundled jars before build as required
rm -f java/tests/lib/commons-logging.jar
rm -f java/tests/lib/log4j-1.2.15.jar
rm -f java/tests/lib/junit-4.4.jar

echo fixing permissions ...
find . -type f -perm /0111 \
    \( -name \*.cpp -or -name \*.h -or -name \*.yy -or -name \*.ll -or \
       -name \*.html -or -name README \) -print -exec chmod 0644 {} \;

%build
aclocal -I tests/m4
autoconf
automake --copy --no-force
%configure \
    --disable-static \
    --enable-contrib \
    --with-quiet-nan \
    --with-java=%{java_home}
# patch libtool to remove rpaths
sed -i 's|^hardcode_into_libs=.*|hardcode_into_libs=no|g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%check
# The test binaries need LD_LIBRARY_PATH to find the compiled fastbit library
# in the build tree.
%make_build LD_LIBRARY_PATH="%{buildroot}%{_libdir};%{_libdir}" check

%install
%make_install

# move jar file to _jnidir, as required
install -d -m 0755 %{buildroot}%{_jnidir}
mv %{buildroot}%{_libdir}/fastbitjni.jar %{buildroot}%{_jnidir}/%{name}.jar
chmod 0644 %{buildroot}%{_jnidir}/%{name}.jar

# move JNI shared library to _libdir/name, as required
install -d -m 0755 %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_libdir}/libfastbitjni.so %{buildroot}%{_libdir}/%{name}/

# remove libtool archives
find %{buildroot} -name \*.la | xargs rm -f

%ldconfig_scriptlets
%ldconfig_scriptlets -n devel

%files
%doc NEWS README
%license COPYING
%{_docdir}/%{name}/*.html
%{_bindir}/ardea
%{_bindir}/fbmerge
%{_bindir}/ibis
%{_bindir}/rara
%{_bindir}/tcapi
%{_bindir}/thula
%{_bindir}/tiapi
%{_libdir}/libfastbit.so.*

%files devel
%dir %{_prefix}/include/%{name}
%{_prefix}/include/%{name}/*.{h,hh}
%{_bindir}/fastbit-config
%{_libdir}/libfastbit.so

%files java
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libfastbitjni.so
%{_jnidir}/%{name}.jar

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.0.3-17
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Feb 5 2020 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-16
- Exclude arch s390x

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-14
- Rebuild for unretire
- License is BSD only

* Fri Sep 6 2019 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-13
- Remove unnecessary build dependencies
- Improve packaging conformance

* Wed Jun 19 2019 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-12
- Use make_build macro instead of make

* Wed Jun 19 2019 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-11
- Replace __make macro with make

* Wed Jun 19 2019 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-10
- Stop using autotools macros that were removed from rpm

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-7
- Add BuildRequires javapackages-tools for needed rpm macros

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.0.3-6
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Sat Feb 10 2018 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-5
- Use new ldconfig_scriptlets macro.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-3
- Ensure linkage to pthread (for ld flag -z defs).

* Wed Dec 20 2017 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-2
- Fix minor typos in spec.

* Tue Oct 10 2017 Philip Kovacs <pkfed@fedoraproject.org> - 2.0.3-1
- Packaging for Fedora.
