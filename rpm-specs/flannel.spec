# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 1
# Run tests in check section
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         coreos
%global repo            flannel
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          317b7d199e3fe937f04ecb39beed025e47316430
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global devel_main      flannel-devel
%global k8s_commit      44368db9916cc345ebef8b6fbde3cdf0dc9d79dc

Name:           flannel 
Version:        0.9.0
Release:        7%{?dist}
Summary:        Etcd address management agent for overlay networks
License:        ASL 2.0 
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
#Source0:        https://%{import_path}/archive/v%{version}.tar.gz
Source1:        flanneld.sysconf
Source2:        flanneld.service
Source3:        flannel-docker.conf
Source4:        flannel-tmpfiles.conf

Patch1:         change-coreos.com-network-to-atomic.io-network-in-he.patch

ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 ppc64le s390x

BuildRequires:      golang >= 1.2.7
%if ! 0%{?with_bundled}
BuildRequires:      golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:      golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires:      golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:      golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:      golang(github.com/aws/aws-sdk-go/service/ec2)
BuildRequires:      golang(github.com/coreos/etcd/client)
BuildRequires:      golang(github.com/coreos/etcd/pkg/transport)
BuildRequires:      golang(github.com/coreos/go-iptables/iptables)
BuildRequires:      golang(github.com/coreos/go-systemd/activation)
BuildRequires:      golang(github.com/coreos/go-systemd/daemon)
BuildRequires:      golang(github.com/coreos/pkg/flagutil)
BuildRequires:      golang(github.com/golang/glog)
BuildRequires:      golang(github.com/gorilla/mux)
BuildRequires:      golang(github.com/jonboulle/clockwork)
BuildRequires:      golang(github.com/vishvananda/netlink)
BuildRequires:      golang(github.com/vishvananda/netlink/nl)
BuildRequires:      golang(golang.org/x/net/context)
BuildRequires:      golang(golang.org/x/oauth2)
BuildRequires:      golang(golang.org/x/oauth2/google)
BuildRequires:      golang(google.golang.org/api/compute/v1)
BuildRequires:      golang(google.golang.org/api/googleapi)
#BuildRequires:      golang(k8s.io/kubernetes/pkg/api)
#BuildRequires:      golang(k8s.io/kubernetes/pkg/client/cache)
#BuildRequires:      golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset)
#BuildRequires:      golang(k8s.io/kubernetes/pkg/client/restclient)
#BuildRequires:      golang(k8s.io/kubernetes/pkg/controller/framework)
#BuildRequires:      golang(k8s.io/kubernetes/pkg/runtime)
#BuildRequires:      golang(k8s.io/kubernetes/pkg/util/runtime)
#BuildRequires:      golang(k8s.io/kubernetes/pkg/util/wait)
#BuildRequires:      golang(k8s.io/kubernetes/pkg/watch)
%endif

BuildRequires:      pkgconfig(systemd)
Requires:           systemd
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description
Flannel is an etcd driven address management agent. Most commonly it is used to
manage the ip addresses of overlay networks between systems running containers
that need to communicate with one another.

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/ec2)
BuildRequires: golang(github.com/coreos/etcd/client)
BuildRequires: golang(github.com/coreos/etcd/pkg/transport)
BuildRequires: golang(github.com/coreos/go-iptables/iptables)
BuildRequires: golang(github.com/coreos/go-systemd/activation)
BuildRequires: golang(github.com/coreos/go-systemd/daemon)
BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/gorilla/mux)
BuildRequires: golang(github.com/jonboulle/clockwork)
BuildRequires: golang(github.com/vishvananda/netlink)
BuildRequires: golang(github.com/vishvananda/netlink/nl)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(google.golang.org/api/compute/v1)
BuildRequires: golang(google.golang.org/api/googleapi)
#BuildRequires: golang(k8s.io/kubernetes/pkg/api)
#BuildRequires: golang(k8s.io/kubernetes/pkg/client/cache)
#BuildRequires: golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset)
#BuildRequires: golang(k8s.io/kubernetes/pkg/client/restclient)
#BuildRequires: golang(k8s.io/kubernetes/pkg/controller/framework)
#BuildRequires: golang(k8s.io/kubernetes/pkg/runtime)
#BuildRequires: golang(k8s.io/kubernetes/pkg/util/runtime)
#BuildRequires: golang(k8s.io/kubernetes/pkg/util/wait)
#BuildRequires: golang(k8s.io/kubernetes/pkg/watch)
%endif

Requires: golang(github.com/aws/aws-sdk-go/aws)
Requires: golang(github.com/aws/aws-sdk-go/aws/awserr)
Requires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
Requires: golang(github.com/aws/aws-sdk-go/aws/session)
Requires: golang(github.com/aws/aws-sdk-go/service/ec2)
Requires: golang(github.com/coreos/etcd/client)
Requires: golang(github.com/coreos/etcd/pkg/transport)
Requires: golang(github.com/coreos/go-iptables/iptables)
Requires: golang(github.com/coreos/go-systemd/activation)
Requires: golang(github.com/coreos/go-systemd/daemon)
Requires: golang(github.com/golang/glog)
Requires: golang(github.com/gorilla/mux)
Requires: golang(github.com/jonboulle/clockwork)
Requires: golang(github.com/vishvananda/netlink)
Requires: golang(github.com/vishvananda/netlink/nl)
Requires: golang(golang.org/x/net/context)
Requires: golang(golang.org/x/oauth2)
Requires: golang(golang.org/x/oauth2/google)
Requires: golang(google.golang.org/api/compute/v1)
Requires: golang(google.golang.org/api/googleapi)
#Requires: golang(k8s.io/kubernetes/pkg/api)
#Requires: golang(k8s.io/kubernetes/pkg/client/cache)
#Requires: golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset)
#Requires: golang(k8s.io/kubernetes/pkg/client/restclient)
#Requires: golang(k8s.io/kubernetes/pkg/controller/framework)
#Requires: golang(k8s.io/kubernetes/pkg/runtime)
#Requires: golang(k8s.io/kubernetes/pkg/util/runtime)
#Requires: golang(k8s.io/kubernetes/pkg/util/wait)
#Requires: golang(k8s.io/kubernetes/pkg/watch)

Provides: golang(%{import_path}/backend) = %{version}-%{release}
Provides: golang(%{import_path}/backend/alloc) = %{version}-%{release}
Provides: golang(%{import_path}/backend/awsvpc) = %{version}-%{release}
Provides: golang(%{import_path}/backend/gce) = %{version}-%{release}
Provides: golang(%{import_path}/backend/hostgw) = %{version}-%{release}
Provides: golang(%{import_path}/backend/udp) = %{version}-%{release}
Provides: golang(%{import_path}/backend/vxlan) = %{version}-%{release}
Provides: golang(%{import_path}/network) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/ip) = %{version}-%{release}
Provides: golang(%{import_path}/remote) = %{version}-%{release}
Provides: golang(%{import_path}/subnet) = %{version}-%{release}
Provides: golang(%{import_path}/subnet/kube) = %{version}-%{release}
Provides: golang(%{import_path}/version) = %{version}-%{release}
Provides: bundled(golang(k8s.io/kubernetes/pkg/api)) = %{k8s_commit}
Provides: bundled(golang(k8s.io/kubernetes/pkg/client/cache)) = %{k8s_commit}
Provides: bundled(golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset)) = %{k8s_commit}
Provides: bundled(golang(k8s.io/kubernetes/pkg/client/restclient)) = %{k8s_commit}
Provides: bundled(golang(k8s.io/kubernetes/pkg/controller/framework)) = %{k8s_commit}
Provides: bundled(golang(k8s.io/kubernetes/pkg/runtime)) = %{k8s_commit}
Provides: bundled(golang(k8s.io/kubernetes/pkg/util/runtime)) = %{k8s_commit}
Provides: bundled(golang(k8s.io/kubernetes/pkg/util/wait)) = %{k8s_commit}
Provides: bundled(golang(k8s.io/kubernetes/pkg/watch)) = %{k8s_commit}

%description devel
Flannel is an etcd driven address management agent. Most commonly it is used to
manage the ip addresses of overlay networks between systems running containers
that need to communicate with one another.

This package contains library source intended for
building other packages which use %{project}/%{repo}.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}
%patch1 -p1

find . -name "*.go" \
       -print |\
              xargs sed -i 's/github.com\/coreos\/flannel\/Godeps\/_workspace\/src\///g'

%build
mkdir -p src/github.com/coreos
ln -s ../../../ src/github.com/coreos/flannel

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{gopath}
%else
# take aws/aws-sdk-go from bundled deps
mv vendor/github.com/aws src/github.com/.
rm -rf vendor
export GOPATH=$(pwd):$(pwd)/Godeps/_workspace:%{gopath}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**}; 
%endif

export LDFLAGS="-X github.com/coreos/flannel/version.Version=%{version}"

%gobuild -o bin/flanneld %{import_path}

%install
# package with binary
install -D -p -m 755 bin/flanneld %{buildroot}%{_bindir}/flanneld
install -D -p -m 644 %{SOURCE1} %{buildroot}/etc/sysconfig/flanneld
install -D -p -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/flanneld.service
install -D -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/docker.service.d/flannel.conf
install -D -p -m 755 dist/mk-docker-opts.sh %{buildroot}%{_libexecdir}/flannel/mk-docker-opts.sh
install -D -p -m 0755 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf

mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}/

%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/Godeps/_workspace:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/pkg/ip
#%%gotest %%{import_path}/remote
%gotest %{import_path}/subnet
%endif

%post
%systemd_post flanneld.service

%preun
# clean tempdir and workdir on removal or upgrade
%systemd_preun flanneld.service

%postun
%systemd_postun_with_restart flanneld.service

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc CONTRIBUTING.md MAINTAINERS README.md DCO NOTICE
%{_bindir}/flanneld
%{_unitdir}/flanneld.service
%{_unitdir}/docker.service.d/flannel.conf
%{_libexecdir}/flannel/mk-docker-opts.sh
%dir %{_libexecdir}/flannel
%config(noreplace) %{_sysconfdir}/sysconfig/flanneld
%dir /run/%{name}/
%{_tmpfilesdir}/%{name}.conf

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTING.md MAINTAINERS README.md DCO NOTICE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%endif

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.9.0-4
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.9.0-1
- Update to 9.0.0
  resolves: #1443517

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.7.0-2
- Fix flanneld --version
  related: #1412005

* Wed Jan 11 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.7.0-1
- Bump to 0.7.0
  resolves: #1412005

* Tue Jan 03 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.6.2-2
- Patch pkg/ip to build and run on s390x
  resolves: #1348906

* Tue Dec 13 2016 Jan Chaloupka <jchaloup@redhat.com> - 0.6.2-1
- Update to 0.6.2
  resolves: #1396472

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-8
- https://fedoraproject.org/wiki/Changes/golang1.7

* Wed Jun 29 2016 jchaloup <jchaloup@redhat.com> - 0.5.5-7
- Own /usr/libexec/flannel directory
- make envs in service and config file canonical

* Fri Jun 03 2016 jchaloup <jchaloup@redhat.com> - 0.5.5-6
- Patch the flannel to use newer version of aws-sdk-go and etcd
  resolves: #1342146

* Sat Apr  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.5-5
- Add support for aarch64

* Thu Mar 10 2016 jchaloup <jchaloup@redhat.com> - 0.5.5-4
- Add support for ppc64le
  resolves: #1316645

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 jchaloup <jchaloup@redhat.com> - 0.5.5-1
- Update to v0.5.5
  resolves: #1281771

* Fri Oct 30 2015 jchaloup <jchaloup@redhat.com> - 0.5.4-3
- Add After=network-online.target and Wants=network-online.target
  to actively wait for network to get on

* Fri Oct 30 2015 jchaloup <jchaloup@redhat.com> - 0.5.4-2
- Add Restart=on-failure to flanned.service file

* Tue Oct 20 2015 jchaloup <jchaloup@redhat.com> - 0.5.4-1
- Update to v0.5.4
  resolves: #1273211

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0.5.3-6
- Make flannel start after the network is ready

* Wed Sep 23 2015 jchaloup <jchaloup@redhat.com> - 0.5.3-5
- Flannel now owns /run/flannel directory

* Wed Sep 23 2015 jchaloup <jchaloup@redhat.com> - 0.5.3-4
- Send systemd notification when -listen is used
- Create /run/flannel directory for mk-docker-opts.sh

* Thu Sep 17 2015 jchaloup <jchaloup@redhat.com> - 0.5.3-3
- Change coreos.com/network to atomic.io/network in help and docs

* Thu Sep 10 2015 jchaloup <jchaloup@redhat.com> - 0.5.3-2
- Change 4001 port in flannel --help and README.md as well

* Mon Aug 31 2015 jchaloup <jchaloup@redhat.com> - 0.5.3-1
- Update to 0.5.3
  resolves: #1258876

* Tue Jul 21 2015 jchaloup <jchaloup@redhat.com> - 0.5.1-3
- Change etcd port from 4001 to 2379
- Polish spec file

* Fri Jul 10 2015 jchaloup <jchaloup@redhat.com> - 0.5.1-2
- Change flannel prefix from /coreos.com/network to /atomic.io/network

* Fri Jul 10 2015 jchaloup <jchaloup@redhat.com> - 0.5.1-1
- Update to 0.5.1

* Fri Jul 10 2015 jchaloup <jchaloup@redhat.com> - 0.5.0-3
- Add After=etcd.service to flanneld.service

* Fri Jun 26 2015 jchaloup <jchaloup@redhat.com> - 0.5.0-2
- Add missing Requires: golang(github.com/gorilla/mux) to devel subpackage

* Fri Jun 26 2015 jchaloup <jchaloup@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 jchaloup <jchaloup@redhat.com> - 0.4.1-2
- Bump to upstream 9180d9a37e2ae6d7fceabea51c6416767c6b50f6
  related: #1223445

* Wed May 20 2015 jchaloup <jchaloup@redhat.com> - 0.4.1-1
- Bump to upstream 4ab27ddd3e87eb2daf152513c0b1dc22879393a8
  resolves: #1223445

* Fri Apr 10 2015 Eric Paris <eparis@redhat.com> - 0.3.1-1
- Bump to version 0.3.1

* Tue Apr 7 2015 Eric Paris <eparis@redhat.com> - 0.3.0-1
- Bump to version 0.3.0

* Mon Mar 30 2015 jchaloup <jchaloup@redhat.com> - 0.2.0-7
- Add debug info
  related: #1165688

* Fri Feb 20 2015 jchaloup <jchaloup@redhat.com> - 0.2.0-6
- Update [Build]Requires for go-etcd package

* Wed Jan 21 2015 Eric Paris <eparis@redhat.com> - 0.2.0-5
- Add generator more like upstream wants to use, use ExecStartPost
  (https://github.com/coreos/flannel/pull/85)

* Tue Jan 20 2015 Eric Paris <eparis@redhat.com> - 0.2.0-4
- Add generator to turn flannel env vars into docker flags

* Tue Jan 20 2015 Peter Lemenkov <lemenkov@gmail.com> - 0.2.0-3
- Change (Build)Requires accordning to the recent changes
  (http://pkgs.fedoraproject.org/cgit/golang-github-coreos-go-systemd.git/commit/?id=204f61c)

* Fri Jan 16 2015 Peter Lemenkov <lemenkov@gmail.com> - 0.2.0-2
- Change flannel service type to notify. See
  https://github.com/coreos/flannel/blob/v0.2.0/main.go#L213

* Tue Dec 23 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.0-1
- update to upstream v0.2.0
- append FLANNEL_OPTIONS variable to unitfile command
- systemd-units merged into systemd for fedora18+

* Tue Dec  2 2014 John W. Linville <linville@redhat.com> - 0.1.0-8.gita7b435a
- Remove patches related to out-of-tree slice backend
- Update to latest upstream

* Thu Nov 20 2014 jchaloup <jchaloup@redhat.com> - 0.1.0-7.git071d778
- Removing deps on Godeps and adding deps on golang-github packages
- Removing wait-online service and changing Type of flannel.service from simple to notify
- Adding README and other doc files
- Adding spec file header with commit, import_path, ...
- Adding devel subpackage
- spec polished based on Lokesh' notes (3 lines below)
- modify summary in specfile as in bug description (capitalize if needed)
- might need to enforce NVR for coreos/go-systemd in deps
- pkgconfig(systemd) is preferable to systemd in BR (I think)
  resolves: #1165688

* Fri Nov 07 2014 - Neil Horman <nhoramn@tuxdriver.com> 
- Updating to latest upstream 

* Fri Nov 07 2014 - Neil Horman <nhoramn@tuxdriver.com> 
- Added wait-online service to sync with docker

* Thu Nov 06 2014 - Neil Horman <nhoramn@tuxdriver.com> 
- Fixed flanneld.service file
- Added linvilles slice type patch

* Tue Nov 04 2014 - Neil Horman <nhorman@tuxdriver.com> - 0.1.0-20141104gitdc530ce
- Initial Build

