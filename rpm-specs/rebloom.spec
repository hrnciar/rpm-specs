Name:		rebloom
Version:	1.1.0
Release:	5%{?dist}
Summary:	Bloom Filter Module for Redis

# Commit ID for latest goodform fix (not released)
# https://fedoraproject.org/wiki/Packaging:SourceURL "Commit Revision"
%global commit 6f8f0f68b678fe1964104c07ea1cd3ad7e6b145b
%global short_commit %(c=%{commit}; echo ${c:0:7})

# Testing issues on certain architectures
%ifarch i686 s390 s390x armv7hl ppc64
%global disable_tests 1
%else
%global disable_tests 0
%endif

License:	AGPLv3
URL:		https://github.com/goodform
Source0:	https://github.com/goodform/%{name}/archive/%{commit}/%{name}-%{version}-%{short_commit}.tar.gz

BuildRequires:  gcc
BuildRequires:	redis-devel
BuildRequires:	python3
BuildRequires:	python3-rmtest >= 1
BuildRequires:	redis >= 4
Requires:	redis(modules_abi)%{?_isa} = %{redis_modules_abi}
Requires:	redis >= 4

%description
This provides a scalable bloom filter as a Redis data type.
Bloom filters are probabilistic data structures that do a very good
job at quickly determining if something is contained within a set.

%prep
%setup -q

%build
%set_build_flags
%make_build LD="gcc"

%if !%{disable_tests}
%check
make PYTHON="python3" test
%endif

%install
mkdir -p %{buildroot}%{redis_modules_dir}
install -pDm755 %{name}.so %{buildroot}%{redis_modules_dir}/%{name}.so

%files
%license LICENSE
%doc README.md docs/index.md docs/Bloom_Commands.md docs/Cuckoo_Commands.md docs/Quick_Start.md
%{redis_modules_dir}/%{name}.so

%changelog
* Mon Feb 17 2020 Nathan Scott <nathans@redhat.com> - 1.1.0-5
- Update the upstream sources for gcc 10 fix (BZ 1799968)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Nathan Scott <nathans@redhat.com> - 1.1.0-1
- Update dependencies for python3 and latest rmtest package.
- Update the upstream sources (https://github.com/goodform).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.3-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Nathan Scott <nathans@redhat.com> - 1.0.3-2
- Remove python installation assumptions.

* Mon Nov 27 2017 Nathan Scott <nathans@redhat.com> - 1.0.3-1
- Add runtime testing using python-rmtest package.
- Update to latest upstream release.

* Fri Nov 17 2017 Nathan Scott <nathans@redhat.com> - 1.0.1-1
- Update use of RPM license macro (from package review).
- Update to latest upstream release.

* Sun Oct 01 2017 Nathan Scott <nathans@redhat.com> - 1.0.0-1
- Initial package
