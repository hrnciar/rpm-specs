%if 0%{?fedora} || 0%{?rhel} == 6
%global with_debug 1
%global with_check 1
%else
%global with_debug 0
%global with_check 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         estesp
%global repo            manifest-tool
# https://github.com/estesp/manifest-tool
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit         a28af2b6bf3748859149bf161eb0630e677c3906
%global shortcommit    %(c=%{commit}; echo ${c:0:7})

Name:           manifest-tool
Version:        1.0.2
Release:        1%{?dist}
#Release:        5.git%{shortcommit}%{?dist}
Summary:        A command line tool used for creating manifest list objects
License:        ASL 2.0
URL:            https://%{provider_prefix}
#Source:         https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source:         https://%{provider_prefix}/%{repo}-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64 ppc64le s390x
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  git make
Provides:       %{repo} = %{version}-%{release}
Provides:       bundled(golang(github.com/codegangsta/cli)) = v1.2.0
Provides:       bundled(golang(github.com/sirupsen/logrus)) = 8bdbc7bcc01dcbb8ec23dc8a28e332258d25251f
Provides:       bundled(golang(github.com/vbatts/tar-split)) = 620714a4c508c880ac1bdda9c8370a2b19af1a55
Provides:       bundled(golang(github.com/gorilla/mux))
Provides:       bundled(golang(golang.org/x/net)) = f3200d17e092c607f615320ecaad13d87ad9a2b3
Provides:       bundled(golang(golang.org/x/time)) = fbb02b2291d28baffd63558aa44b4b56f178d650
Provides:       bundled(golang(golang.org/x/sys)) = 4c4f7f33c9ed00de01c4c741d2177abfcfe19307
Provides:       bundled(golang(golang.org/x/crypto)) = 88737f569e3a9c7ab309cdc09a07fe7fc87233c3
Provides:       bundled(golang(github.com/go-yaml/yaml)) = v2
Provides:       bundled(golang(github.com/docker/cli)) = 18.09
Provides:       bundled(golang(github.com/docker/docker)) = 71e07f91307a9cb51071c6510768139c1f436750
Provides:       bundled(golang(github.com/docker/docker-credential-helpers)) = 5241b46610f2491efdf9d1c85f1ddf5b02f6d962
Provides:       bundled(golang(github.com/docker/distribution)) = 0d3efadf0154c2b8a4e7b6621fff9809655cc580
Provides:       bundled(golang(github.com/opencontainers/go-digest)) = 279bed98673dd5bef374d3b6e4b09e2af76183bf
Provides:       bundled(golang(github.com/docker/go-connections)) = 7395e3f8aa162843a74ed6d48e79627d9792ac55
Provides:       bundled(golang(github.com/docker/go-units)) = 519db1ee28dcc9fd2474ae59fca29a810482bfb1
Provides:       bundled(golang(github.com/docker/go-metrics)) = d466d4f6fd960e01820085bd7e1a24426ee7ef18
Provides:       bundled(golang(github.com/docker/libtrust)) = 9cbd2a1374f46905c68a4eb3694a130610adc62a
Provides:       bundled(golang(github.com/opencontainers/runc)) = 3e425f80a8c931f88e6d94a8c831b9d5aa481657
Provides:       bundled(golang(github.com/opencontainers/runtime-spec)) = 29686dbc5559d93fb1ef402eeda3e35c38d75af4
Provides:       bundled(golang(github.com/opencontainers/image-spec)) = d60099175f88c47cd379c4738d158884749ed235
Provides:       bundled(golang(github.com/prometheus/client_golang)) = c5b7fccd204277076155f10851dad72b76a49317
Provides:       bundled(golang(github.com/prometheus/client_model)) = 6f3806018612930941127f2a7c6c453ba2c527d2
Provides:       bundled(golang(github.com/prometheus/common)) = 7600349dcfe1abd18d72d3a1770870d9800a7801
Provides:       bundled(golang(github.com/prometheus/procfs)) = 7d6f385de8bea29190f15ba9931442a0eaef9af7
Provides:       bundled(golang(github.com/beorn7/perks)) = e7f67b54abbeac9c40a31de0f81159e4cafebd6a
Provides:       bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = c12348ce28de40eed0136aa2b644d0ee0650e56c
Provides:       bundled(golang(google.golang.org/grpc)) = v1.12.0
Provides:       bundled(golang(google.golang.org/genproto)) = d80a6e20e776b0b17a324d0ba1ab50a39c8e8944
Provides:       bundled(golang(github.com/pkg/errors)) = ba968bfe8b2f7e042a574c888954fccecfa385b4
Provides:       bundled(golang(github.com/gogo/protobuf)) = v1.0.0
Provides:       bundled(golang(github.com/golang/protobuf)) = v1.1.0
Provides:       bundled(golang(github.com/Azure/go-ansiterm)) = d6e3b3328b783f23731bc4d058875b0371ff8109
Provides:       bundled(golang(github.com/Microsoft/hcsshim)) = 672e52e9209d1e53718c1b6a7d68cc9272654ab5
Provides:       bundled(golang(github.com/Microsoft/go-winio)) = 6c72808b55902eae4c5943626030429ff20f3b63
Provides:       bundled(golang(github.com/konsorten/go-windows-terminal-sequences)) = f55edac94c9bbba5d6182a4be46d86a2c9b5b50e
Provides:       bundled(golang(github.com/mattn/go-shellwords))
Provides:       bundled(golang(github.com/containerd/containerd)) = 9754871865f7fe2f4e74d43e2fc7ccd237edcbce
Provides:       bundled(golang(github.com/containerd/continuity)) = 004b46473808b3e7a4a3049c20e4376c91eb966d
Provides:       bundled(golang(golang.org/x/sync)) = e225da77a7e68af35c70ccbf71af2b83e6acac3c
Provides:       bundled(golang(github.com/morikuni/aec)) = 39771216ff4c63d11f5e604076f9c45e8be1067b

%description
This tool was mainly created for the purpose of viewing, creating, and
pushing the new manifests list object type in the Docker registry. Manifest
lists are defined in the v2.2 image specification and exist mainly for the
purpose of supporting multi-architecture and/or multi-platform images within
a Docker registry.

%prep
#autosetup -Sgit -n %{name}-%{commit}
%autosetup -n %{name}-%{version}

%build
mkdir _build
pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s $(dirs +1 -l) src/%{import_path}
popd

export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
make binary

%install
export GOPATH=$(pwd)/_build:$(pwd):%{gopath}
make DESTDIR=%{buildroot} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Mon Apr 06 2020 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 release

* Mon Mar 09 2020 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.rc2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.rc2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 22 2019 Josh Boyer <jwboyer@fedoraproject.org> - 1.0.0-0.rc2
- Update to 1.0.0-rc2 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Josh Boyer <jwboyer@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0 upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5.gita28af2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4.gita28af2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Josh Boyer <jwboyer@fedoraproject.org> 0.6.0-3.gita28af2b
- Add bundled provides (rhbz 1467322)

* Wed Jul 05 2017 Josh Boyer <jwboyer@fedoraproject.org> 0.6.0-2.gita28af2b
- Cleanup with_bundled and license macro definitions (rhbz 1467322)

* Sun Jul 02 2017 Josh Boyer <jwboyer@fedoraproject.org> 0.6.0-1.gita28af2b
- Initial package for manifest-tool
