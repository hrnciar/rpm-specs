# This is the commit that bumped the version to v28, without a tag.
%global commit 9190005e32c6151b76ac707b30eeb4d5d9dd1d36
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global pforth_datadir %{_datadir}/%{name}-%{version}
%global pforth_default_dic %{pforth_datadir}/pforth.dic

Name:           pforth
Version:        28
Release:        5%{?dist}
Summary:        Portable ANS-like Forth

License:        Public Domain
URL:            http://www.softsynth.com/pforth/
Source0:        https://github.com/philburk/pforth/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  gcc make

%description
pForth is a portable implementation of the Forth language. It provides ANS
standard support for Core, Core Extensions, File-Access, Floating-Point,
Locals, Programming-Tools, Strings word sets.


%prep
%setup -q -n %{name}-%{commit}


%build
# no _smp_mflags: ../../csrc/pf_save.c:42:14: fatal error: pfdicdat.h: No such file or directory
make -C build/unix DEBUGOPTS= \
        EXTRA_CCOPTS='%{optflags} -DPF_DEFAULT_DICTIONARY=\"%{pforth_default_dic}\" \
                -Wno-builtin-macro-redefined -D__DATE__=\"release\" -D__TIME__=\"%{release}\"'


%check
make -C build/unix test


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{pforth_datadir}

install build/unix/pforth %{buildroot}%{_bindir}
install -pm644 build/unix/pforth.dic %{buildroot}%{pforth_datadir}


%files
%{_bindir}/pforth
%{pforth_datadir}
%doc readme.txt
%doc releases.txt


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 28-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Lubomir Rintel <lkundrak@v3.sk> - 28-1
- Initial packaging
