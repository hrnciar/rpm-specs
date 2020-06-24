#
# Currently debuginfo breaks the build.
#
# I get one of the following two failures following recommended debuginfo
# methods for golang:
#
#   *** ERROR: No build ID note found in /builddir/build/BUILDROOT/reg-0.4.1-1.x86_64/usr/bin/reg-server
#
# or:
#
#   /var/tmp/rpm-tmp.U9Lwrk: line 36: syntax error near unexpected token `)'
#
%global debug_package %{nil}

# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0

# modifying the Go binaries breaks the DWARF debugging
%global __os_install_post %{_rpmconfigdir}/brp-compress

%global provider_prefix github.com/genuinetools/reg
%global import_path     %{provider_prefix}
#global commit          8d8ca405f7a8c8c4f72686ed239c767aba663f9b
#global shortcommit     %%(c=%%{commit}; echo ${c:0:7})

Name:       reg
Version:    0.15.5
Release:    5%{?dist}
Summary:    Docker registry v2 command line client


License:    MIT
URL:        https://%{import_path}/%{name}

Source0:    https://github.com/genuinetools/reg/archive/v%{version}.tar.gz

# Upstream advertises this as something that's meant to be run in a container
# and doesn't provide a systemd unit or sysV init script or sysconfig files
# so I'm providing them here.
Source1:    reg-server.service
Source2:    sysconfig.reg-server

BuildRequires: golang
BuildRequires: systemd

%if 0%{?epel}
# The version of golang is too old to understand the vendor manifest and can't
# find the appropriate path for the vendored version of this.
BuildRequires: golang-github-gorilla-context-devel

# For whatever reason golang-github-gorilla-context-devel isn't available in
# EPEL for any of the other arches.
#   BZ filed: https://bugzilla.redhat.com/show_bug.cgi?id=1466521
ExclusiveArch: x86_64
%endif

# The following section is populated by parsing the Gopkg.lock file
# at the base dir of a git checkout of the source code.
#
#   $ git clone https://github.com/jessfraz/reg.git
#   $ cd reg
#
# Bundled Provides are defined as per Fedora Guidelines:
#   https://fedoraproject.org/wiki/Packaging:Guidelines#Bundling_and_Duplication_of_system_libraries
#
Provides: bundled(golang(github.com/Azure/go-ansiterm)) = d6e3b3328b783f23731bc4d058875b0371ff8109
Provides: bundled(golang(github.com/Microsoft/go-winio)) = 67921128fb397dd80339870d2193d6b1e6856fd4
Provides: bundled(golang(github.com/Nvveen/Gotty)) = cd527374f1e5bff4938207604a14f2e38a9cf512
Provides: bundled(golang(github.com/beorn7/perks)) = 3a771d992973f24aa725d07868b467d1ddfceafb
Provides: bundled(golang(github.com/containerd/continuity)) = 0377f7d767206f3a9e8881d0f02267b0d89c7a62
Provides: bundled(golang(github.com/coreos/clair)) = 9a9b1f7a13fa1cb796fe6dfb45ed241f39ce9f01
Provides: bundled(golang(github.com/docker/cli)) = b395d2d6f5eec2c047e6bba4a3fd941d5757d725
Provides: bundled(golang(github.com/docker/distribution)) = 749f6afb4572201e3c37325d0ffedb6f32be8950
Provides: bundled(golang(github.com/docker/docker)) = 492545e139e7461aac044149a931bb4b2dd48f75
Provides: bundled(golang(github.com/docker/docker-ce)) = 2ec1cede27a3dc04c44f8ed2feb1efb00c724d63
Provides: bundled(golang(github.com/docker/docker-credential-helpers)) = 5241b46610f2491efdf9d1c85f1ddf5b02f6d962
Provides: bundled(golang(github.com/docker/go-connections)) = 7395e3f8aa162843a74ed6d48e79627d9792ac55
Provides: bundled(golang(github.com/docker/go-metrics)) = 399ea8c73916000c64c2c76e8da00ca82f8387ab
Provides: bundled(golang(github.com/docker/go-units)) = 47565b4f722fb6ceae66b95f853feed578a4a51c
Provides: bundled(golang(github.com/docker/libtrust)) = aabc10ec26b754e797f9028f4589c5b7bd90dc20
Provides: bundled(golang(github.com/genuinetools/pkg)) = 3654fc151753f8cd41b366e0c15b9fa070890ddf
Provides: bundled(golang(github.com/gogo/protobuf)) = 7d68e886eac4f7e34d0d82241a6273d6c304c5cf
Provides: bundled(golang(github.com/golang/protobuf)) = b4deda0973fb4c70b50d226b1af49f3da59f5265
Provides: bundled(golang(github.com/google/go-cmp)) = 3af367b6b30c263d47e8895973edcca9a49cf029
Provides: bundled(golang(github.com/gorilla/context)) = 08b5f424b9271eedf6f9f0ce86cb9396ed337a42
Provides: bundled(golang(github.com/gorilla/mux)) = e3702bed27f0d39777b0b37b664b6280e8ef8fbf
Provides: bundled(golang(github.com/grpc-ecosystem/grpc-gateway)) = 92583770e3f01b09a0d3e9bdf64321d8bebd48f2
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = c12348ce28de40eed0136aa2b644d0ee0650e56c
Provides: bundled(golang(github.com/mitchellh/go-wordwrap)) = ad45545899c7b13c020ea92b2072220eefad42b8
Provides: bundled(golang(github.com/opencontainers/go-digest)) = c9281466c8b2f606084ac71339773efd177436e7
Provides: bundled(golang(github.com/opencontainers/image-spec)) = d60099175f88c47cd379c4738d158884749ed235
Provides: bundled(golang(github.com/opencontainers/runc)) = baf6536d6259209c3edfa2b22237af82942d3dfa
Provides: bundled(golang(github.com/peterhellberg/link)) = d1cebc7ea14a5fc0de7cb4a45acae773161642c6
Provides: bundled(golang(github.com/pkg/errors)) = 645ef00459ed84a119197bfb8d8205042c6df63d
Provides: bundled(golang(github.com/prometheus/client_golang)) = bcbbc08eb2ddff3af83bbf11e7ec13b4fd730b6e
Provides: bundled(golang(github.com/prometheus/client_model)) = 5c3871d89910bfb32f5fcab2aa4b9ec68e65a99f
Provides: bundled(golang(github.com/prometheus/common)) = 7600349dcfe1abd18d72d3a1770870d9800a7801
Provides: bundled(golang(github.com/prometheus/procfs)) = ae68e2d4c00fed4943b5f6698d504a5fe083da8a
Provides: bundled(golang(github.com/sirupsen/logrus)) = c155da19408a8799da419ed3eeb0cb5db0ad5dbc
Provides: bundled(golang(golang.org/x/crypto)) = a49355c7e3f8fe157a85be2f77e6e269a0f89602
Provides: bundled(golang(golang.org/x/net)) = d0887baf81f4598189d4e12a37c6da86f0bba4d0
Provides: bundled(golang(golang.org/x/sys)) = ac767d655b305d4e9612f5f6e33120b9176c4ad4
Provides: bundled(golang(golang.org/x/text)) = f21a4dfb5e38f5895301dc265a8def02365cc3d0
Provides: bundled(golang(google.golang.org/genproto)) = e92b116572682a5b432ddd840aeaba2a559eeff1
Provides: bundled(golang(google.golang.org/grpc)) = 168a6198bcb0ef175f7dacec0b8691fc141dc9b8
Obsoletes: reg-server < %{version}

%description
Docker registry v2 client.

%prep
%setup -q -n %{name}-%{version}

# Have to move things around because of how golang likes to search $GOPATH
cd ../
mv $OLDPWD hack
mkdir $OLDPWD
cd $OLDPWD
mkdir -p $(pwd)/go/src/%{import_path}
mv ../hack/* $(pwd)/go/src/%{import_path}/

# Have to mess with the pathing even more to make the older version of golang
# in el7 happy.
%if 0%{?epel}
for d in $(ls $(pwd)/go/src/%{import_path}/vendor/)
do
    if [[ -d "$(pwd)/go/src/%{import_path}/vendor/${d}" ]]; then
        printf "D VALUE: %s\n" "${d}"
        mkdir -p $(pwd)/go/src/${d}
        cp -r $(pwd)/go/src/%{import_path}/vendor/${d}/* $(pwd)/go/src/${d}/
    fi
done
%endif

%build
export GOPATH="$(pwd)/go:%{buildroot}%{gopath}:%{gopath}"

cd $(pwd)/go/src/%{import_path}/

# Leave this here for when we can sort out the debuginfo fix
#   https://bugzilla.redhat.com/show_bug.cgi?id=1432214
#go build \
#    -ldflags '-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d \' \\n\')' \
#    -o reg .
#
#go build \
#    -ldflags '-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d \' \\n\')' \
#    -o reg-server ./server

go build -o reg .

%install

# Install the binaries
cd ./go/src/%{import_path}/
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

# Install templates and static content
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}-server
install -d server/templates/ %{buildroot}/%{_sharedstatedir}/%{name}-server/templates/
install -d server/static/ %{buildroot}%{_sharedstatedir}/%{name}-server/static/
cp -p -r server/templates/* %{buildroot}%{_sharedstatedir}/%{name}-server/templates/
cp -p -r server/static/* %{buildroot}%{_sharedstatedir}/%{name}-server/static/

# Install the systemd unit
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}-server.service

# Install the sysconfig file
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0640 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-server


mkdir -p %{buildroot}/%{name}-%{version}

# Setup doc files for doc macro
for i in README.md Dockerfile Makefile
do
    cp -p ${i} %{_builddir}/%{name}-%{version}/
done

# Setup license file for license macro
cp -p LICENSE %{_builddir}/%{name}-%{version}/

%post
%systemd_post %{name}-server.service

%preun
%systemd_preun %{name}-server.service

%postun
%systemd_postun %{name}-server.service

%files
%doc README.md Dockerfile Makefile
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}-server.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-server
%config(noreplace) %{_sharedstatedir}/%{name}-server/static/
%config(noreplace) %{_sharedstatedir}/%{name}-server/templates/

%changelog
* Thu Apr 23 2020 Mattia Verga <mattia.verga@protonmail.com> - 0.15.5-5
- Fix %%postun directive

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Kevin Fenzi <kevin@scrye.com> - 0.15.5-1
- Update to 0.15.5

* Thu Jul 26 2018 Kevin Fenzi <kevin@scrye.com> - 0.15.4-1
- Update to 0.15.4.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.4.1-5
- Actually apply the patch for single-run execution

* Thu Jun 29 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.4.1-4
- Fix epel7 build

* Tue Jun 27 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.4.1-3
- Add patch to allow single-run execution of reg-server for static html
  generation

* Mon Jun 19 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.4.1-2
- Add ghost file entry for statically generated index.html

* Mon Jun 12 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.4.1-1
- Update to latest upstream
- Switch to using upstream versioning, they are tagging versions now.

* Tue Mar 21 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.2.0-2.git.0.94d0af5
- Move static/templates and systemd workingdir to /var/lib/reg-server
- Change Source0 to point to github archive url instead of local git-archive
- Fix tabs vs spaces in the spec file

* Tue Mar 14 2017 Adam Miller <maxamillion@fedoraproject.org> - 0.2.0-1.git.0.94d0af5
- First package for Fedora
