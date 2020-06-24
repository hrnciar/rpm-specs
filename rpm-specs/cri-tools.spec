%global with_bundled 1
%global with_check 0

%if 0%{?fedora} > 28
%global with_debug 0
%else
%global with_debug 1
%endif

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

# %if ! 0% {?gobuild:1}
%define gobuild(o:) go build -tags="$BUILDTAGS selinux seccomp" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
#% endif

%global provider github
%global provider_tld com
%global project kubernetes-incubator
%global repo %{name}
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path %{provider_prefix}
%global commit0 19b7255f328e447150adc4ab6a62999189ec447d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: cri-tools
Version: 1.11.0
Release: 5.dev.git%{shortcommit0}%{?dist}
Summary: CLI and validation tools for Container Runtime Interface
License: ASL 2.0
URL: https://%{provider_prefix}
Source0: https://%{provider_prefix}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# no ppc64
ExclusiveArch: %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: glibc-static
BuildRequires: git
BuildRequires: go-md2man
Provides: crictl = %{version}-%{release}

# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' vendor.conf | sort
# [thanks to Carl George <carl@george.computer> for containerd.spec]
Provides: bundled(golang(github.com/docker/distribution)) = edc3ab29cdff8694dd6feb85cfeb4b5f1b38ed9c
Provides: bundled(golang(github.com/docker/docker)) = 4f3616fb1c112e206b88cb7a9922bf49067a7756
Provides: bundled(golang(github.com/docker/go-units)) = 9e638d38cf6977a37a8ea0078f3ee75a7cdb2dd1
Provides: bundled(golang(github.com/docker/spdystream)) = 449fdfce4d962303d702fec724ef0ad181c92528
Provides: bundled(golang(github.com/emicklei/go-restful)) = ff4f55a206334ef123e4f79bbf348980da81ca46
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = f12c6236fe7b5cf6bcf30e5935d08cb079d78334
Provides: bundled(golang(github.com/ghodss/yaml)) = 73d445a93680fa1a78ae23a5839bad48f32ba1ee
Provides: bundled(golang(github.com/gogo/protobuf)) = c0656edd0d9eab7c66d1eb0c568f9039345796f7
Provides: bundled(golang(github.com/golang/glog)) = 44145f04b68cf362d9c4df2182967c2275eaefed
Provides: bundled(golang(github.com/golang/protobuf)) = 4bd1920723d7b7c925de087aa32e2187708897f7
Provides: bundled(golang(github.com/google/btree)) = 316fb6d3f031ae8f4d457c6c5186b9e3ded70435
Provides: bundled(golang(github.com/google/gofuzz)) = 44d81051d367757e1c7c6a5a86423ece9afcf63c
Provides: bundled(golang(github.com/go-openapi/jsonpointer)) = 46af16f9f7b149af66e5d1bd010e3574dc06de98
Provides: bundled(golang(github.com/go-openapi/jsonreference)) = 13c6e3589ad90f49bd3e3bbe2c2cb3d7a4142272
Provides: bundled(golang(github.com/go-openapi/spec)) = 6aced65f8501fe1217321abf0749d354824ba2ff
Provides: bundled(golang(github.com/go-openapi/swag)) = 1d0bd113de87027671077d3c71eb3ac5d7dbba72
Provides: bundled(golang(github.com/gregjones/httpcache)) = c1f8028e62adb3d518b823a2f8e6a95c38bdd3aa
Provides: bundled(golang(github.com/json-iterator/go)) = f8eb43eda36e882db58fb97d663a9357a379b547
Provides: bundled(golang(github.com/juju/ratelimit)) = 5b9ff866471762aa2ab2dced63c9fb6f53921342
Provides: bundled(golang(github.com/mailru/easyjson)) = d5b7844b561a7bc640052f1b935f7b800330d7e0
Provides: bundled(golang(github.com/onsi/ginkgo)) = 67b9df7f55fe1165fd9ad49aca7754cce01a42b8
Provides: bundled(golang(github.com/onsi/gomega)) = d59fa0ac68bb5dd932ee8d24eed631cdd519efc3
Provides: bundled(golang(github.com/opencontainers/selinux)) = b29023b86e4a69d1b46b7e7b4e2b6fda03f0b9cd
Provides: bundled(golang(github.com/pborman/uuid)) = ca53cad383cad2479bbba7f7a1a05797ec1386e4
Provides: bundled(golang(github.com/peterbourgon/diskv)) = 5f041e8faa004a95c88a202771f4cc3e991971e6
Provides: bundled(golang(github.com/PuerkitoBio/purell)) = v1.0.0
Provides: bundled(golang(github.com/PuerkitoBio/urlesc)) = 5bd2802263f21d8788851d5305584c82a5c75d7e
Provides: bundled(golang(github.com/spf13/pflag)) = 9ff6c6923cfffbcd502984b8e0c80539a94968b7
Provides: bundled(golang(github.com/ugorji/go)) = ded73eae5db7e7a0ef6f55aace87a2873c5d2b74
Provides: bundled(golang(github.com/urfave/cli)) = 7fb9c86b14e6a702a4157ccb5a863f07d844a207
Provides: bundled(golang(golang.org/x/crypto)) = 81e90905daefcd6fd217b62423c0908922eadb30
Provides: bundled(golang(golang.org/x/net)) = 1c05540f6879653db88113bc4a2b70aec4bd491f
Provides: bundled(golang(golang.org/x/sys)) = 7ddbeae9ae08c6a06a59597f0c9edbc5ff2444ce
Provides: bundled(golang(golang.org/x/text)) = b19bf474d317b857955b12035d2c5acb57ce8b01
Provides: bundled(golang(google.golang.org/genproto)) = 09f6ed296fc66555a25fe4ce95173148778dfa85
Provides: bundled(golang(google.golang.org/grpc)) = v1.3.0
Provides: bundled(golang(gopkg.in/inf.v0)) = v0.9.0
Provides: bundled(golang(gopkg.in/yaml.v2)) = 53feefa2559fb8dfa8d81baad31be332c97d6c77
Provides: bundled(golang(k8s.io/api)) = 218912509d74a117d05a718bb926d0948e531c20
Provides: bundled(golang(k8s.io/apimachinery)) = 18a564baac720819100827c16fdebcadb05b2d0d
Provides: bundled(golang(k8s.io/client-go)) = 72e1c2a1ef30b3f8da039e92d4a6a1f079f374e8
Provides: bundled(golang(k8s.io/kube-openapi)) = 39a7bf85c140f972372c2a0d1ee40adbf0c8bfe1
Provides: bundled(golang(k8s.io/kubernetes)) = 164317879bcd810b97e5ebf1c8df041770f2ff1b
Provides: bundled(golang(k8s.io/utils)) = bf963466fd3fea33c428098b12a89d8ecd012f2

%description
%{summary}

%prep
%autosetup -Sgit -n %{name}-%{commit0}

%build
mkdir _build
pushd _build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../../ src/%{import_path}
popd
ln -s vendor src
export GOPATH=$(pwd)/_build:$(pwd):$(pwd):%{gopath}

GOPATH=$GOPATH %gobuild -o bin/crictl %{import_path}/cmd/crictl
go-md2man -in docs/crictl.md -out docs/crictl.1

%install
# install binaries
install -dp %{buildroot}%{_bindir}
install -p -m 755 ./bin/crictl %{buildroot}%{_bindir}

# install manpage
install -dp %{buildroot}%{_mandir}/man1
install -p -m 644 docs/crictl.1 %{buildroot}%{_mandir}/man1

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md OWNERS README.md RELEASE.md code-of-conduct.md
%doc docs/{benchmark.md,roadmap.md,validation.md}
%{_bindir}/crictl
%{_mandir}/man1/crictl*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-5.dev.git19b7255
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-4.dev.git19b7255
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3.dev.git19b7255
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.11.0-2.dev.git19b7255
- autobuilt 19b7255

* Tue Jul 17 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.11.0-1.dev.gitf95ba2f
- bump to v1.11.0
- built f95ba2f

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - version.Versionversion.Version-2.git41d6c4a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - version.Versionversion.Version-1.git41d6c4a1
- bump to version.Version
- autobuilt 41d6c4a

* Fri Jun 29 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - crictlVersion-3.git3bf77bf
- autobuilt 3bf77bf

* Wed Jun 27 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - crictlVersion-2.git012eea1
- autobuilt 012eea1

* Tue Jun 19 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - crictlVersion-1.git78ec590
- bump to crictlVersion
- autobuilt 78ec590

* Sat Jun 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-26.git9c667f5
- autobuilt 9c667f5

* Fri Jun 15 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-25.gitc38159e
- autobuilt c38159e

* Fri Jun 08 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-24.git9da2549
- autobuilt 9da2549

* Sun May 27 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-23.giteae53b2
- autobuilt eae53b2

* Fri May 25 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-22.gitc58160c
- autobuilt c58160c

* Fri May 18 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-21.gitb2cb253
- autobuilt b2cb253

* Wed May 09 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-20.git6ae7b25
- autobuilt 6ae7b25

* Tue May 08 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-19.gited19775
- autobuilt ed19775

* Fri May 04 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-18.git585e558
- autobuilt 585e558

* Wed May 02 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-17.git49847ed
- autobuilt commit 49847ed

* Fri Apr 27 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-16.git34ce008
- autobuilt commit 34ce008

* Tue Apr 24 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-15.git0dca09b
- autobuilt commit 0dca09b

* Sat Apr 21 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-14.gitf37a5a1
- autobuilt commit f37a5a1

* Thu Apr 19 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-13.gitdb53d78
- autobuilt commit db53d78

* Tue Apr 17 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-12.gitf6ed14e
- autobuilt commit f6ed14e

* Tue Apr 17 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-11.gitf6ed14e
- autobuilt commit f6ed14e

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-10.gitf6ed14e
- autobuilt commit f6ed14e

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-9.gitf6ed14e
- autobuilt commit f6ed14e

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-8.gitf6ed14e
- autobuilt commit f6ed14e

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-7.gitf6ed14e
- autobuilt commit f6ed14e

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-6.gitf6ed14e
- autobuilt commit f6ed14e

* Fri Apr 06 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-5.gitf6ed14e
- built commit f6ed14e

* Mon Mar 26 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-4.git207e773
- built commit 207e773

* Mon Mar 26 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-3.git653cc8c
- disable critest cause PITA to build

* Wed Feb 07 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-2.alpha.0.git653cc8c
- include critest binary

* Wed Feb 07 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-1.alpha.0.gitf1a58d6
- First package for Fedora

