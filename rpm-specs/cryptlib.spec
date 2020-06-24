%global includetests 0
# 0=no, 1=yes
%global cryptlibdir %{_libdir}/%{name}
%global withpython2 0

Name:       cryptlib
Version:    3.4.5  
Release:    10%{?dist}
Summary:    Security library and toolkit for encryption and authentication services    

License:    Sleepycat and OpenSSL     
URL:        https://www.cs.auckland.ac.nz/~pgut001/cryptlib      
Source0:    https://crypto-bone.com/fedora/cl345_fedora.zip      
Source1:    https://crypto-bone.com/fedora/cl345_fedora.zip.sig
# for security reasons a public signing key should always be stored in distgit
# and never be used with a URL to make impersonation attacks harder
# (verified: https://senderek.ie/keys/codesigningkey)
Source2:    gpgkey-3274CB29956498038A9C874BFBF6E2C28E9C98DD.asc
Source3:    https://crypto-bone.com/fedora/README-manual
Source4:    https://crypto-bone.com/fedora/cryptlib-tests.tar.gz
Source5:    https://crypto-bone.com/fedora/cryptlib-perlfiles.tar.gz

# soname is now libcl.so.3.4
Patch1:     ccflagspatch
Patch2:     javapatch
Patch3:     perlpatch
Patch4:     gccversionpatch

ExclusiveArch: x86_64 %{ix86} aarch64 ppc64 ppc64le

BuildRequires: gcc 
BuildRequires: libbsd-devel   
BuildRequires: gnupg2
BuildRequires: coreutils
BuildRequires: python3-devel
BuildRequires: java-devel
BuildRequires: perl-interpreter
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-Data-Dumper
BuildRequires: perl-ExtUtils-MakeMaker


%if %{withpython2}
    BuildRequires: python2-devel >= 2.7
%endif


%description
Cryptlib is a powerful security toolkit that allows even inexperienced crypto
programmers to easily add encryption and authentication services to their
software. The high-level interface provides anyone with the ability to add
strong security capabilities to an application in as little as half an hour,
without needing to know any of the low-level details that make the encryption
or authentication work.  Because of this, cryptlib dramatically reduces the
cost involved in adding security to new or existing applications.

At the highest level, cryptlib provides implementations of complete security
services such as S/MIME and PGP/OpenPGP secure enveloping, SSL/TLS and
SSH secure sessions, CA services such as CMP, SCEP, RTCS, and OCSP, and other
security operations such as secure time-stamping. Since cryptlib uses
industry-standard X.509, S/MIME, PGP/OpenPGP, and SSH/SSL/TLS data formats,
the resulting encrypted or signed data can be easily transported to other
systems and processed there, and cryptlib itself runs on virtually any
operating system - cryptlib doesn't tie you to a single system.
This allows email, files and EDI transactions to be authenticated with
digital signatures and encrypted in an industry-standard format.


%package devel
Summary:  Cryptlib application development files 
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and code for application development in C (and C++)


%package test
Summary:  Cryptlib test program
Requires: %{name}%{?_isa} = %{version}-%{release}

%description test
Cryptlib test programs for C, Java, Perl and Python3


%package java
Summary:  Cryptlib bindings for Java
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: java-headless

%description java
Cryptlib module for application development in Java


%package javadoc
Summary:  Cryptlib Java documentation
Buildarch : noarch

%description javadoc
Cryptlib Javadoc information

%if %{withpython2}
    %package python2
    Summary:  Cryptlib bindings for python2
    Group:    System Environment/Libraries
    Requires: %{name}%{?_isa} = %{version}-%{release}
    Requires: python2 >= 2.7
    %description python2
    Cryptlib module for application development in Python 2
%endif

%package python3
Summary:  Cryptlib bindings for python3
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3 >= 3.5  

%description python3
Cryptlib module for application development in Python3

%package perl
Summary:  Cryptlib bindings for perl
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: man

%description perl
Cryptlib module for application development in Perl



%prep
# source code signature check with GnuPG
KEYRING=$(echo %{SOURCE2})
KEYRING=${KEYRING%%.asc}.gpg
mkdir -p .gnupg
gpg2 --homedir .gnupg --no-default-keyring --quiet --yes --output $KEYRING --dearmor  %{SOURCE2}
gpg2 --homedir .gnupg --no-default-keyring --keyring $KEYRING --verify %{SOURCE1} %{SOURCE0}

rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
/usr/bin/unzip -a %{SOURCE0}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# remove pre-build jar file
rm %{_builddir}/%{name}-%{version}/bindings/cryptlib.jar
# adapt perl files in bindings
cd %{_builddir}/%{name}-%{version}/bindings
/usr/bin/tar xpzf %{SOURCE5}

%build
cd %{name}-%{version}
chmod +x tools/mkhdr.sh

tools/mkhdr.sh

# rename cryptlib symbols that may collide with openssl symbols
chmod +x tools/rename.sh
tools/rename.sh
# build java bindings
cp /etc/alternatives/java_sdk/include/jni.h .
cp /etc/alternatives/java_sdk/include/linux/jni_md.h .

make clean
make shared %{?_smp_mflags} ADDFLAGS="%{optflags}"
ln -s libcl.so.3.4.5 libcl.so
ln -s libcl.so libcl.so.3.4
make stestlib %{?_smp_mflags} ADDFLAGS="%{optflags}"

# build python modules
cd bindings
%if %{withpython2}
     python2 setup.py build
%endif
python3 setup.py build

# build javadoc
mkdir javadoc
cd javadoc
jar -xf ../cryptlib.jar
javadoc cryptlib


%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}
cp %{_builddir}/%{name}-%{version}/libcl.so.3.4.5 %{buildroot}%{_libdir}
cd %{buildroot}%{_libdir}
ln -s libcl.so.3.4.5 libcl.so.3.4
ln -s libcl.so.3.4 libcl.so

# install header files
mkdir -p %{buildroot}/%{_includedir}/%{name}
cp %{_builddir}/%{name}-%{version}/crypt.h %{buildroot}%{_includedir}/%{name}
cp %{_builddir}/%{name}-%{version}/cryptkrn.h %{buildroot}%{_includedir}/%{name}
cp %{_builddir}/%{name}-%{version}/cryptlib.h %{buildroot}%{_includedir}/%{name}

# add Java bindings
mkdir -p %{buildroot}/%{cryptlibdir}/java
mkdir -p %{buildroot}/usr/lib/java
cp %{_builddir}/%{name}-%{version}/bindings/cryptlib.jar %{buildroot}/usr/lib/java

# install docs
cp %{_builddir}/%{name}-%{version}/COPYING %{buildroot}%{_datadir}/licenses/%{name}
cp %{_builddir}/%{name}-%{version}/README %{buildroot}%{_docdir}/%{name}/README
echo "No tests performed." > %{_builddir}/%{name}-%{version}/stestlib.log
cp %{_builddir}/%{name}-%{version}/stestlib.log %{buildroot}%{_docdir}/%{name}/stestlib.log
cp %{SOURCE3} %{buildroot}%{_docdir}/%{name}

# install javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
rm -rf %{_builddir}/%{name}-%{version}/bindings/javadoc/META-INF
cp -r %{_builddir}/%{name}-%{version}/bindings/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%if %{withpython2}
     # install python2 module
     mkdir -p %{buildroot}%{python2_sitelib}
     cp %{_builddir}/%{name}-%{version}/bindings/build/lib.linux-*%{python2_version}/cryptlib_py.so %{buildroot}%{python2_sitelib}
%endif

# install python3 module
mkdir -p %{buildroot}%{python3_sitelib}
cp %{_builddir}/%{name}-%{version}/bindings/build/lib.linux-*%{python3_version}/cryptlib_py.cpython-3*-%{_arch}-linux-gnu.so %{buildroot}%{python3_sitelib}/cryptlib_py.so

# install Perl module
mkdir -p %{buildroot}/usr/local/lib64
mkdir -p %{buildroot}%{_libdir}/perl5
mkdir -p %{buildroot}%{_mandir}/man3
cd %{_builddir}/%{name}-%{version}/bindings
mkdir -p %{_builddir}/include
cp ../cryptlib.h %{_builddir}/include
cp ../tools/GenPerl.pl .
export PERL_CRYPT_LIB_HEADER=%{_builddir}/include/cryptlib.h
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
sed -i '/LDLOADLIBS = /s/thread/thread -L.. -lcl/' Makefile
make
make pure_install DESTDIR=%{buildroot}
# clean the install
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name 'PerlCryptLib.so' -exec chmod 0755 {} \;

# install test programs
cp %{_builddir}/%{name}-%{version}/stestlib %{buildroot}%{cryptlibdir}
cp -r %{_builddir}/%{name}-%{version}/test %{buildroot}%{cryptlibdir}/test
# remove all c code from the test directory
rm -rf $(find %{buildroot}%{cryptlibdir}/test -name "*.c")

# extract test files
cd %{buildroot}%{cryptlibdir}
tar xpzf %{SOURCE4} 

%check
# checks are performed after install
# in KOJI tests must be disabled as there is no networking
%if %{includetests}
     cd %{_builddir}/%{name}-%{version}
     ln -s libcl.so.3.4.5 ./libcl.so.3.4
     export LD_LIBRARY_PATH=.
     echo "Running tests on the cryptlib library. This will take a few minutes."
     echo "Network access is necessary to complete all tests!"
     ./stestlib > %{_builddir}/%{name}-%{version}/stestlib.log
     cp %{_builddir}/%{name}-%{version}/stestlib.log %{buildroot}%{_docdir}/%{name}/stestlib.log
%endif


%ldconfig_scriptlets


%files
%{_libdir}/libcl.so.3.4.5
%{_libdir}/libcl.so.3.4
%{_libdir}/libcl.so

%license   %{_datadir}/licenses/%{name}/COPYING
%doc       %{_docdir}/%{name}/README
%doc       %{_docdir}/%{name}/stestlib.log
%doc       %{_docdir}/%{name}/README-manual


%files devel
%{_libdir}/libcl.so
%{_includedir}/%{name}/crypt.h
%{_includedir}/%{name}/cryptkrn.h
%{_includedir}/%{name}/cryptlib.h

%files java
/usr/lib/java/cryptlib.jar

%files javadoc
%{_javadocdir}/%{name}

%if %{withpython2}
     %files python2
     %{python2_sitelib}/cryptlib_py.so
%endif

%files python3
%{python3_sitelib}/cryptlib_py.so

%files perl
%{_libdir}/perl5
%{_mandir}/man3/PerlCryptLib.3pm.gz

%files test
%{cryptlibdir}


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-10
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Ralf Senderek <innovation@senderek.ie> - 3.4.5-8
- gcc-10: remove deprecated flag -mcpu (RHBZ #1793394)

* Sat Nov 23 2019 Ralf Senderek <innovation@senderek.ie> - 3.4.5-7
- Enable gcc versions > 9

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.5-4
- Perl 5.30 rebuild

* Fri May 24 2019 Ralf Senderek <innovation@senderek.ie> - 3.4.5-3
- Update Perl installation paths

* Mon Mar 18 2019 Ralf Senderek <innovation@senderek.ie> - 3.4.5-2
- Removing obsolete conflict with beignet

* Sun Mar 10 2019 Ralf Senderek <innovation@senderek.ie> - 3.4.5-1
- Update to version 3.4.5 and porting to python3 only

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Ralf Senderek <innovation@senderek.ie> - 3.4.4-11
- Remove python2 module (RHBZ #1634602)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Petr Pisar <ppisar@redhat.com> - 3.4.4-9
- Perl 5.28 rebuild

* Wed Jul 04 2018 Ralf Senderek <innovation@senderek.ie> - 3.4.4-8
- Force use of python2 in mkhdr.sh

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 3.4.4-7
- Perl 5.28 rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.4-6
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.4-5
- Rebuilt for Python 3.7

* Sun May 27 2018 Ralf Senderek <innovation@senderek.ie> - 3.4.4-4
- Fix Java jar path

* Fri Apr 20 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 3.4.4-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Ralf Senderek <innovation@senderek.ie> - 3.4.4-1
- Update to version 3.4.4

* Wed Aug 09 2017 Senderek Web Security <innovation@senderek.ie> - 3.4.3.1-7
- update configuration code for powerpc64

* Wed Aug 02 2017 Senderek Web Security <innovation@senderek.ie> - 3.4.3.1-6
- include ppc64/ppc64le and introducing the new python3 module

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Senderek Web Security <innovation@senderek.ie> - 3.4.3.1-3
- include aarch64 and exclude ppc64 

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.3.1-2
- Perl 5.26 rebuild

* Sat Feb 11 2017 Senderek Web Security <innovation@senderek.ie> - 3.4.3.1-1
- update to version 3.4.3.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Senderek Web Security <innovation@senderek.ie> - 3.4.3-9
- compile with gcc-7.0 and -march=native

* Tue Jul 26 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-8
- change license tag (RHBZ #1352406)
- rename symbols that collide with openssl (RHBZ #1352404)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 16 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-6
- Remove perl-generators for epel7
- Remove python3 script from test subpackage (fixes RHBZ #1347294)

* Tue Jun 14 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-5
- Fix source locations
- Clean up perl file installation
- Fix python3 module code in spec file

* Thu Jun 9 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-4
- Removed the doc subpackage

* Mon Jun 6 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-3
- Fixed Java subpackage dependency
- Made devel arch specific

* Fri Jun 3 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-2
- Added javadoc subpackage and made docs noarch
- Added a perl subpackage
- Modified native stestlib program with two tests disabled
  (testSessionSSH and testSessionSSHClientCert)

* Wed Jun 1 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-1
- Added python2/python3 subpackage
- Source code signature check with GnuPG enabled

* Sun May 29 2016 Senderek Web Security <innovation@senderek.ie> - 3.4-2
- Added doc and java subpackage

* Fri May 27 2016 Senderek Web Security <innovation@senderek.ie> - 3.4-1
- Initial version of the rpm package build
