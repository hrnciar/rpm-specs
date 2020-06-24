%bcond_with tests

Name:           triehash
Version:        0.3
Release:        3%{?dist}
Summary:        Generator for order-preserving minimal perfect hash functions in C

License:        MIT
URL:            https://jak-linux.org/projects/triehash/
Source0:        https://github.com/julian-klode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%if %{with tests}
BuildRequires:  perl(Devel::Cover)
%endif
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl-generators

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
TrieHash generates perfect hash functions as C code which then gets
compiled into optimal machine code as part of the usual program compilation.

TrieHash works by translating a list of strings to a trie, and then converting
the trie to a set of recursive switch statements; first switching by length,
and then switching by bytes.

TrieHash has various optimizations such as processing multiple bytes at once
(on GNU C), and shortcuts for reducing the complexity of case-insensitive
matching (ASCII only). Generated code performs substantially faster than
gperf, but is larger.

TrieHash was written for use in APT.


%prep
%autosetup


%build
pod2man triehash.pl triehash.1


%install
install -p -m755 -D triehash.pl %{buildroot}%{_bindir}/%{name}
install -p -m644 -D triehash.1 %{buildroot}%{_mandir}/man1/%{name}.1

%if %{with tests}
%check
./tests/run-tests.sh
%endif

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*



%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.3-3
- Perl 5.32 rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Neal Gompa <ngompa13@gmail.com> - 0.3-1
- Initial packaging for Fedora (RH#1764799)
