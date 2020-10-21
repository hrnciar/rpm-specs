%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 1
%global with_bundled 1
%global with_debug 0
%global with_check 1
%global with_unit_test 1
%else
%global with_devel 0
%global with_bundled 1
%global with_debug 0
%global with_check 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%global provider        github
%global provider_tld    com
%global project         openshift
%global repo            source-to-image
# https://github.com/openshift/source-to-image
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          226afa1319c3498f47b974ec8ceb36526341a19c
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global majorFromGit    1
%global minorFromGit    0+
%global versionFromGit  v1.0.9
%global commitFromGit   %{commit}


Name:           %{repo}
Version:        1.1.7
Release:        8%{?dist}
Summary:        A tool for building artifacts from source and injecting into docker images
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# there is no docker on ppc64, only on ppc64le
# https://bugzilla.redhat.com/show_bug.cgi?id=1465159
ExcludeArch: ppc64
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%if ! 0%{?with_bundled}
BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/pflag)
%endif

Requires:      docker
Requires:      git
Requires:      tar

Provides:      s2i = %{version}-%{release}

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/pflag)
%endif

Requires:      golang(github.com/golang/glog)
Requires:      golang(github.com/spf13/cobra)
Requires:      golang(github.com/spf13/pflag)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/api) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/api/describe) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/api/validation) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/build) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/build/ignore) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/build/strategies) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/build/strategies/layered) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/build/strategies/onbuild) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/build/strategies/sti) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/cmd) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/config) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/create) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/create/templates) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/docker) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/docker/test) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/errors) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/ignore) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/run) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/scm) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/scm/empty) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/scm/file) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/scm/git) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/scripts) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/tar) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/test) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/util) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/util/user) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/version) = %{version}-%{release}
Provides:      golang(%{import_path}/test/integration) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test
Summary:         Unit tests for %{name} package
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build
mkdir -p src/github.com/openshift
ln -s ../../../ src/github.com/openshift/source-to-image

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{gopath}
%else
export GOPATH=$(pwd):$(pwd)/Godeps/_workspace:%{gopath}
%endif

export STI_GIT_MAJOR=1.0
export STI_GIT_MINOR=2
export STI_GIT_VERSION=%{commit}

export LDFLAGS="\
	-X %{import_path}/pkg/version.majorFromGit=%{majorFromGit} \
	-X %{import_path}/pkg/version.minorFromGit=%{minorFromGit} \
	-X %{import_path}/pkg/version.versionFromGit=%{versionFromGit} \
	-X %{import_path}/pkg/version.commitFromGit=%{commitFromGit}"
%gobuild -o bin/s2i %{import_path}/cmd/s2i

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 bin/s2i %{buildroot}%{_bindir}

# source codes for building projects
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
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
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

%gotest %{import_path}/pkg/api
%gotest %{import_path}/pkg/api/validation
%gotest %{import_path}/pkg/build/strategies/layered
%gotest %{import_path}/pkg/build/strategies/onbuild
%gotest %{import_path}/pkg/build/strategies/sti
%gotest %{import_path}/pkg/docker
%gotest %{import_path}/pkg/ignore
#%%gotest %%{import_path}/pkg/scm
#%gotest %{import_path}/pkg/scm/git
%gotest %{import_path}/pkg/scripts
%gotest %{import_path}/pkg/tar
%gotest %{import_path}/pkg/util
%gotest %{import_path}/pkg/util/user
%gotest %{import_path}/test/integration
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md AUTHORS
%{_bindir}/s2i

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md AUTHORS
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md AUTHORS
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Jan Chaloupka <jchaloup@redhat.com> - 1.1.7-5
- Remove unneeded dependency on github.com/fsouza/go-dockerclient
  resolves: #1676016

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.1.7-1
- Update to v1.1.7
  resolves: #1510476

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Till Maas <opensource@till.name> - 1.0.9-5
- Do not build on ppc64 (does not contain docker)

* Mon May 15 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.9-4
- Fix go-1.8 -X importpath/name=value syntax

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sat May 21 2016 jchaloup <jchaloup@redhat.com> - 1.0.9-1
- Update to v1.0.9
  resolves: #1273677

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- New upstream release
- https://github.com/openshift/source-to-image/releases/tag/v1.0.4

* Thu Oct 22 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.3-2
- Rebase to new upstream version
- Package now provides s2i
- Disable tests removed by upstream

* Thu Sep 17 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-4
- Fix dependencies
- Remove -devel sub package

* Tue Sep 15 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-2
- Build the right directory

* Mon Sep 14 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git00d1cb3
- First package for Fedora


