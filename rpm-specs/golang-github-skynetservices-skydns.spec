# Generated by go2rpm
%bcond_without check

# https://github.com/skynetservices/skydns
%global goipath         github.com/skynetservices/skydns
Version:                2.5.3
%global commit          15f42ac021b1f17a8b329f409539aa1624458da0

%gometa

%global common_description %{expand:
DNS service discovery for etcd.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md

Name:           %{goname}
Release:        3.a%{?dist}
Summary:        DNS service discovery for etcd

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        skydns.service
Source2:        skydns.conf
Source3:        skydns.socket
# Fix for new github.com/coreos/go-systemd
Patch0:         0001-Fix-for-new-github.com-coreos-go-systemd.patch
# Remove ErrTruncated, obsolete in new github.com/miekg/dns
Patch1:         0001-Remove-ErrTruncated.patch

BuildRequires:  golang(go.etcd.io/etcd/client)
BuildRequires:  golang(go.etcd.io/etcd/clientv3)
BuildRequires:  golang(go.etcd.io/etcd/mvcc/mvccpb)
BuildRequires:  golang(go.etcd.io/etcd/pkg/transport)
BuildRequires:  golang(github.com/coreos/go-systemd/activation)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  systemd-rpm-macros

%if %{with check}
# Tests
BuildRequires:  golang(golang.org/x/net/context)
%endif

%description
%{common_description}

%package -n skydns
Summary:        DNS service discovery for etcd

Requires:       etcd
Requires(pre):  shadow-utils
Provides:       skydns = %{version}-%{release}

%description -n skydns
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
%patch1 -p1
find . -name "*.go" -exec sed -i "s|github.com/coreos/etcd|go.etcd.io/etcd|" "{}" +;

%build
%gobuild -o %{gobuilddir}/bin/skydns %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/skydns.service
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_unitdir}/skydns.socket
install -dm 0755 %{buildroot}%{_sysconfdir}/skydns
install -m 644 -t %{buildroot}%{_sysconfdir}/skydns %{SOURCE2}
install -dm 0755 %{buildroot}%{_sharedstatedir}/skydns

%pre -n skydns
getent group skydns >/dev/null || groupadd -r skydns
getent passwd skydns >/dev/null || useradd -r -g skydns -d %{_sharedstatedir}/skydns \
        -s /sbin/nologin -c "Skydns user" skydns

%post -n skydns
%systemd_post skydns.service

%preun -n skydns
%systemd_preun skydns.service

%postun -n skydns
%systemd_postun skydns.service

%if %{with check}
%check
# server: needs network
%gocheck -d server
%endif

%files -n skydns
%license LICENSE
%doc AUTHORS CONTRIBUTORS README.md
%{_bindir}/*
%dir %attr(-,skydns,skydns) %{_sharedstatedir}/skydns
%{_unitdir}/skydns.service
%{_unitdir}/skydns.socket
%config(noreplace) %{_sysconfdir}/skydns

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-3.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 14:30:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.5.3-1.a.20190528git15f42ac
- Release 2.5.3a, commit 15f42ac021b1f17a8b329f409539aa1624458da0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-0.10.a.git8688008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-0.9.a.git8688008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-0.8.a.git8688008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-0.7.a.git8688008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-0.6.a.git8688008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-0.5.a.git8688008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-0.4.a.git8688008
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-0.3.a.git8688008
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-0.2.a.git8688008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 jchaloup <jchaloup@redhat.com> - 2.5.3-0.1.a.git8688008
- Update to 2.5.3.a
  related: #1269191

* Wed Oct 21 2015 jchaloup <jchaloup@redhat.com> - 0-0.8.git6c94cbe
- Introduce skydns.docker to be able to bind to port 53 as a skydns user
  resolves: #1269191

* Mon Aug 24 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.git6c94cbe
- Update spec file to spec-2.0
  resolves: #1250508

* Mon Jun 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git6c94cbe
- Update pre, post, preun, postun sections to belong to skydns subpackage
  related: #1181197

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git6c94cbe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git6c94cbe
- Bump to upstream 6c94cbe92349cf550e64752a7cb72c98bcc44325
- Add skydns subpackage with skydns binary
- Add debuginfo
- Move LICENSE under license macro
- Add skydns.service and skydns.conf files
  related: #1181197

* Mon Jan 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git245a121
- Requires on kubernetes makes building of kubernetes failing.
  related: #1181197

* Sun Jan 18 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git245a121
- Fix Requires on kubernetes
  related: #1181197

* Mon Jan 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git245a121
- First package for Fedora
  resolves: #1181197