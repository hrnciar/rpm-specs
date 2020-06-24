# We need to ship both versions of the EPL
# Some plug-ins are moving to EPL 2, but some plug-ins might stay with EPL 1
%global eplv2_ver 2.0.1
%global eplv2_tag org.eclipse.license-license-%{eplv2_ver}.v20180423-1114
%global eplv1_ver 1.0.1
%global eplv1_tag org.eclipse.license-license-%{eplv1_ver}.v20140414-1359

Name:      eclipse-license
Version:   %{eplv2_ver}
Release:   9%{?dist}
Summary:   Shared license features for Eclipse
License:   EPL-1.0 and EPL-2.0
URL:       http://wiki.eclipse.org/CBI
Source1:   http://git.eclipse.org/c/cbi/org.eclipse.license.git/snapshot/%{eplv1_tag}.tar.bz2
Source2:   http://git.eclipse.org/c/cbi/org.eclipse.license.git/snapshot/%{eplv2_tag}.tar.bz2

BuildArch: noarch

# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch: s390 %{arm} %{ix86}

BuildRequires: tycho

%description
Shared license features for Eclipse. Other features may consume these
features to avoid unnecessary duplication of license boiler plate.

%package -n %{name}1
Version:   %{eplv1_ver}
Summary:   Shared EPL v1.0 license feature for Eclipse
License:   EPL-1.0
# Provides/Obsoletes added in F28
Provides:  eclipse-license = %{eplv1_ver}-20
Obsoletes: eclipse-license < %{eplv2_ver}-%{release}

%description -n %{name}1
Shared license feature for Eclipse. Other features may consume this
feature to avoid unnecessary duplication of license boiler plate.

%package -n %{name}2
Version:   %{eplv2_ver}
Summary:   Shared EPL v2.0 license feature for Eclipse
License:   EPL-2.0

%description -n %{name}2
Shared license feature for Eclipse. Other features may consume this
feature to avoid unnecessary duplication of license boiler plate.

%prep
%setup -q -c -T

tar xf %{SOURCE1}
tar xf %{SOURCE2}

%pom_remove_plugin ":tycho-packaging-plugin" */pom.xml

%build
pushd %{eplv1_tag}
%mvn_build -j
popd

pushd %{eplv2_tag}
sed -i -e 's/\(-SNAPSHOT\|\.qualifier\)/.v20180423-1114/' pom.xml */*.xml
%mvn_build -j
popd

%install
pushd %{eplv1_tag}
%mvn_package "::pom::" __noinstall
%mvn_package ":" 1
%mvn_install
popd

# Remove exploded tycho external bundles zipfile in case we are operating
# in bootstrap mode
rm -rf /tmp/tycho-bundles-external*

pushd %{eplv2_tag}
%mvn_package "::pom::" __noinstall
%mvn_package ":" 2
%mvn_install
popd

%files -n %{name}1 -f %{eplv1_tag}/.mfiles-1
%license %{eplv1_tag}/org.eclipse.license/*.html

%files -n %{name}2 -f %{eplv2_tag}/.mfiles-2
%license %{eplv2_tag}/org.eclipse.license/*.html

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Mat Booth <mat.booth@redhat.com> - 2.0.1-7
- Restrict to same architectures as Eclipse itself

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Mat Booth <mat.booth@redhat.com> - 2.0.1-5
- Allow building when tycho is bootstrapped

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Mat Booth <mat.booth@redhat.com> - 2.0.1-3
- Use actual release tag

* Mon Jun 11 2018 Mat Booth <mat.booth@redhat.com> - 2.0.1-2
- Avoid reliance on tycho-extras

* Wed May 30 2018 Mat Booth <mat.booth@redhat.com> - 2.0.1-1
- Ship both EPL v1.0 and EPL v2.0 features

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 25 2015 Mat Booth <mat.booth@redhat.com> - 1.0.1-8
- No need to package pom file

* Tue Jun 30 2015 Mat Booth <mat.booth@redhat.com> - 1.0.1-7
- BR on eclipse-filesystem

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 26 2014 Mat Booth <mat.booth@redhat.com> - 1.0.1-5
- Build/install with xmvn
- Require eclipse-filesystem

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Mat Booth <mat.booth@redhat.com> - 1.0.1-3
- Update to latest upstream.

* Thu Mar 13 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-2
- Use Xmvn.

* Thu Mar 13 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-1
- Initial version of license shared feature.

