################################################################################
Name:             tomcatjss
################################################################################

Summary:          JSS Connector for Apache Tomcat
URL:              http://www.dogtagpki.org/wiki/TomcatJSS
License:          LGPLv2+
BuildArch:        noarch

Version:          7.5.0
Release:          1%{?_timestamp}%{?_commit_id}%{?dist}
#global           _phase -a1

# To generate the source tarball:
# $ git clone https://github.com/dogtagpki/tomcatjss.git
# $ cd tomcatjss
# $ git archive \
#     --format=tar.gz \
#     --prefix tomcatjss-VERSION/ \
#     -o tomcatjss-VERSION.tar.gz \
#     <version tag>
Source:           https://github.com/dogtagpki/tomcatjss/archive/v%{version}%{?_phase}/tomcatjss-%{version}%{?_phase}.tar.gz

# To create a patch for all changes since a version tag:
# $ git format-patch \
#     --stdout \
#     <version tag> \
#     > tomcatjss-VERSION-RELEASE.patch
# Patch: tomcatjss-VERSION-RELEASE.patch
Patch1: 0001-Switch-to-JDK8-source-target-compatibility.patch

################################################################################
# Build Dependencies
################################################################################

# jpackage-utils requires versioning to meet both build and runtime requirements
# jss requires versioning to meet both build and runtime requirements
# tomcat requires versioning to meet both build and runtime requirements

# autosetup
BuildRequires:    git

# Java
BuildRequires:    ant
BuildRequires:    apache-commons-lang
BuildRequires:    java-devel
BuildRequires:    jpackage-utils >= 0:1.7.5-15

# SLF4J
BuildRequires:    slf4j
%if 0%{?rhel} && 0%{?rhel} <= 7
# no slf4j-jdk14
%else
BuildRequires:    slf4j-jdk14
%endif

# JSS
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:    jss >= 4.4.0-7
%else
BuildRequires:    jss >= 4.7.0
%endif

# Tomcat
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:    tomcat >= 7.0.69
%else
%if 0%{?fedora} && 0%{?fedora} <= 27
BuildRequires:    tomcat >= 8.0.49
%else
%if 0%{?fedora} && 0%{?fedora} <= 28
BuildRequires:    tomcat >= 1:8.5.23
%else
%if 0%{?rhel}
BuildRequires:    pki-servlet-engine >= 1:9.0.7
%else
BuildRequires:    tomcat >= 1:9.0.7
%endif
%endif
%endif
%endif

################################################################################
# Runtime Dependencies
################################################################################

# Java
Requires:         apache-commons-lang
%if 0%{?fedora} >= 21
Requires:         java-headless
%else
Requires:         java
%endif
Requires:         jpackage-utils >= 0:1.7.5-15

# SLF4J
Requires:         slf4j
%if 0%{?rhel}
# no slf4j-jdk14
%else
Requires:         slf4j-jdk14
%endif

# JSS
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:         jss >= 4.4.0-7
%else
Requires:         jss >= 4.7.0
%endif

# Tomcat
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:         tomcat >= 7.0.69
%else
%if 0%{?fedora} && 0%{?fedora} <= 27
Requires:         tomcat >= 8.0.49
%else
%if 0%{?fedora} && 0%{?fedora} <= 28
Requires:         tomcat >= 1:8.5.23
%else
%if 0%{?rhel}
Requires:         pki-servlet-engine >= 1:9.0.7
%else
Requires:         tomcat >= 1:9.0.7
%endif
%endif
%endif
%endif

# PKI
Conflicts:        pki-base < 10.6.5


%if 0%{?rhel}
# For EPEL, override the '_sharedstatedir' macro on RHEL
%define           _sharedstatedir    /var/lib
%endif

%description
JSS Connector for Apache Tomcat, installed via the tomcatjss package,
is a Java Secure Socket Extension (JSSE) module for Apache Tomcat that
uses Java Security Services (JSS), a Java interface to Network Security
Services (NSS).

################################################################################
%prep
################################################################################

%autosetup -n tomcatjss-%{version}%{?_phase} -p 1 -S git

################################################################################
%install
################################################################################

# get Tomcat <major>.<minor> version number
tomcat_version=`/usr/sbin/tomcat version | sed -n 's/Server number: *\([0-9]\+\.[0-9]\+\).*/\1/p'`

if [ $tomcat_version == "9.0" ]; then
    app_server=tomcat-8.5
else
    app_server=tomcat-$tomcat_version
fi

ant -f build.xml \
    -Dversion=%{version} \
    -Dsrc.dir=$app_server \
    -Djnidir=%{_jnidir} \
    -Dinstall.doc.dir=%{buildroot}%{_docdir}/%{name} \
    -Dinstall.jar.dir=%{buildroot}%{_javadir} \
    install

################################################################################
%files
################################################################################

%license LICENSE

%defattr(-,root,root)
%doc README
%doc LICENSE
%{_javadir}/*

################################################################################
%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 7.5.0-0.5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jun 10 2020 Dogtag PKI Team <pki-devel@redhat.com> - 7.5.0-0.4
- Rebase to match latest upstream version v7.5.0-b2

* Wed Jun 10 2020 Dogtag PKI Team <pki-devel@redhat.com> - 7.5.0-0.1
- Rebase to match latest upstream version v7.5.0-a1
- Make TomcatJSS use both SunJSSE and Mozilla-JSS

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 08 2019 Dogtag PKI Team <pki-team@redhat.com> - 7.4.1-2
- Bumping min requirement for jss to 4.6.0

* Thu Aug 08 2019 Dogtag PKI Team <pki-team@redhat.com> - 7.4.1-1
- Rebased to TomcatJSS 7.4.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Dogtag PKI Team <pki-team@redhat.com> - 7.4.0-1
- Rebased to TomcatJSS 7.4.0

* Mon May 06 2019 Dogtag PKI Team <pki-team@redhat.com> - 7.3.7-1
- Rebased to Tomcatjss 7.3.7

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Dogtag PKI Team <pki-team@redhat.com> 7.3.6-1
- Rebased to TomcatJSS 7.3.6

* Mon Aug 13 2018 Dogtag PKI Team <pki-team@redhat.com> 7.3.5-1
- Rebased to TomcatJSS 7.3.5

* Tue Aug 07 2018 Dogtag PKI Team <pki-devel@redhat.com> 7.3.4-1
- Rebased to TomcatJSS 7.3.4

* Tue Aug 07 2018 Dogtag PKI Team <pki-devel@redhat.com> 7.3.3-2
- Red Hat Bugzilla #1612063 - Do not override system crypto policy (support TLS 1.3)

* Fri Jul 20 2018 Dogtag PKI Team <pki-devel@redhat.com> 7.3.3-1
- Rebased to TomcatJSS 7.3.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Dogtag PKI Team <pki-devel@redhat.com> 7.3.2-1
- Rebased to TomcatJSS 7.3.2

* Fri Jun 15 2018 Dogtag PKI Team <pki-devel@redhat.com> 7.3.1-1
- Fixed Tomcat dependencies
- Rebased to TomcatJSS 7.3.1

* Thu Apr 12 2018 Dogtag PKI Team <pki-devel@redhat.com> 7.3.0-1
- Cleaned up spec file
- Rebased to TomcatJSS 7.3.0 final

* Thu Mar 15 2018 Dogtag PKI Team <pki-devel@redhat.com> 7.3.0-0.2
- Rebased to TomcatJSS 7.3.0 beta
