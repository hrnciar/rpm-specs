%global with_devel 0
%global with_bundled 1
%global with_debug 1
%global with_check 0
%global with_unit_test 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n') -extldflags '-Wl,-z,relro -Wl,--as-needed  -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld '" -a -v -x %{?**};
%endif

%global provider github
%global provider_tld com
%global project containers
%global repo oci-seccomp-bpf-hook
# https://github.com/containers/oci-seccomp-bpf-hook
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global git0 https://%{import_path}
%global commit0 05a82a1227fb47c34a28537699d3c05e8d4463f8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:8})

# bcc is built only for these arches
ExclusiveArch: x86_64 %{power64} aarch64 s390x

# Used for comparing with latest upstream tag
# to decide whether to autobuild (non-rawhide only)
%define built_tag v1.1.0
%define built_tag_strip %(b=%{built_tag}; echo ${b:1})

Name: oci-seccomp-bpf-hook
Version: 1.1.0
Release: 1.1.git%{shortcommit0}%{?dist}
Summary: OCI Hook to generate seccomp json files based on EBF syscalls used by container
License: ASL 2.0
URL: %{git0}
Source0: %{git0}/archive/%{commit0}/%{repo}-%{shortcommit0}.tar.gz
BuildRequires: golang
BuildRequires: go-md2man
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: bcc-devel
BuildRequires: git
BuildRequires: gpgme-devel
BuildRequires: libseccomp-devel
BuildRequires: make
Enhances: podman
Enhances: cri-o

%description
%{summary}
%{repo} provides a library for applications looking to use
the Container Pod concept popularized by Kubernetes.

%prep
%autosetup -Sgit -n %{repo}-%{commit0}

%build
mkdir _build
pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path}
popd
ln -s vendor src
export GOPATH=$(pwd)/_build:$(pwd)
%gobuild -o bin/%{name} %{import_path}
%{__make} GOMD2MAN=go-md2man -C docs

%install
%{__make} \
      DESTDIR=%{buildroot} \
      PREFIX=%{_prefix} \
      OCI-SECCOMP-BPF_VERSION=%{version} \
      install-nobuild \
      install.docs-nobuild

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
# Since we aren't packaging up the vendor directory we need to link
# back to it somehow. Hack it up so that we can add the vendor
# directory from BUILD dir as a gopath to be searched when executing
# tests from the BUILDROOT dir.
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor

export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/src/%{name}
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%dir %{_libexecdir}/oci
%dir %{_libexecdir}/oci/hooks.d
%{_libexecdir}/oci/hooks.d/%{name}
%dir %{_datadir}/containers
%dir %{_datadir}/containers/oci
%dir %{_datadir}/containers/oci/hooks.d
%{_datadir}/containers/oci/hooks.d/%{name}.json
%{_mandir}/man1/%{name}.1*

%changelog
* Tue May 19 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-1.1.git05a82a1
- bump version
- reuse Makefile targets

* Mon Feb 17 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.0.1-0.6.gitba7bbb16
- Resolves: #1799105 - solve ftbfs and build latest upstream commit

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.5.git3baa603a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Jindrich Novy <jnovy@redhat.com> - 0.0.1-0.4.git3baa603a
- limit arches to only those supported by bcc so that this can be built

* Mon Nov 04 2019 Jindrich Novy <jnovy@redhat.com> - 0.0.1-0.3.git3baa603a
- fix the license - should be ASL 2.0
- use %%gobuild

* Mon Nov 04 2019 Jindrich Novy <jnovy@redhat.com> - 0.0.1-0.2.git3baa603a
- pull in golang deps as BR

* Mon Sep 23 2019 Jindrich Novy <jnovy@redhat.com> - 0.0.1-0.1.git3baa603a
- fix spec file and build

* Sun Sep 22 2019 Dan Walsh <dwalsh@redhat.com> - 0.0.1
- Initial Version
