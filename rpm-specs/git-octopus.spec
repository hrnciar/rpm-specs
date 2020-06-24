# Build project from bundled dependencies
%global with_bundled 0
%global debug_package %{nil}

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%global provider        github
%global provider_tld    com
%global project         lesfurets
%global repo            git-octopus
# https://github.com/lesfurets/git-octopus
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global pre_rel         beta.3

Name:           git-octopus
Version:        2.0
Release:        %{?pre_rel:0.}4%{?pre_rel:.%pre_rel}%{?dist}.4
Summary:        Git commands for continuous delivery
License:        LGPLv3
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}%{?pre_rel:-%pre_rel}/%{name}-%{version}%{?pre_rel:-%pre_rel}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}

Requires:   git >= 1.8
Requires:   %{_bindir}/shasum

# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: asciidoc

%description
The continuous merge workflow is meant for continuous integration/delivery and
is based on feature branching. git-octopus provides git commands to implement
it.

%prep
%setup -q -n %{name}-%{version}%{?pre_rel:-%pre_rel}

%build
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../ src/%{import_path}

export GOPATH=$(pwd):%{gopath}

make %{?_smp_mflags} build-docs 

%gobuild -o bin/git-octopus %{import_path}/

%install
install -d -p %{buildroot}%{_bindir}

install -p -v -m 0755 bin/git-octopus %{buildroot}%{_bindir}

make prefix="%{buildroot}%{_prefix}" \
              docdir="%{buildroot}%{_docdir}/%{name}%{?rhel:-%{version}}" install-docs



%check
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# Since we aren't packaging up the vendor directory we need to link
# back to it somehow. Hack it up so that we can add the vendor
# directory from BUILD dir as a gopath to be searched when executing
# tests from the BUILDROOT dir.
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor

export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%endif

%files
%doc README.md doc/*.html
%license LICENSE
%{_bindir}/git-*
%{_mandir}/man1/git-*.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.4.beta.3.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.4.beta.3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.4.beta.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.4.beta.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Xavier Bachelot <xavier@bachelot.org> - 2.0-0.4.beta3
- Update to 2.0 beta 3.
- Fix Source0: URL (RHBZ#1583361: FTBFS).

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.3.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.2.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Andrea Baita <andrea@baita.pro> - 2.0-0.1.beta2
- package go beta version 2

* Mon Apr 10 2017 Jabouille Jean Charles <jean-charles.jabouille@kelkoo.com> - 2.0-0.1.beta1
- package go beta version

* Mon Jan 30 2017 Andrea Baita <andrea@baita.pro> - 1.4-3
- added ?_smp_mflags 

* Tue Dec 06 2016 Andrea Baita <andrea@baita.pro> - 1.4-2
- added documentation build, updated build requires

* Wed Nov 30 2016 Andrea Baita <andrea@baita.pro> - 1.4-1
- Packaging of version 1.4.

* Thu Nov 17 2016 Xavier Bachelot <xavier@bachelot.org> - 1.3-1
- Initial package.
