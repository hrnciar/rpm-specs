%define upstream_name    Dir-Manifest

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.6.1
Release:    4%{?dist}

Summary:    Load texts or blobs from a directory of files
License:    MIT
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{upstream_name}-%{version}.tar.gz

Requires:  perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
BuildRequires: perl(:VERSION) >= 5.14.0
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Moo)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Socket)
BuildRequires: perl(Test::More)
BuildRequires: perl(blib)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildArch:  noarch

%description
Here is the primary use case: you have several long texts (and/or binary
blobs) that you wish to load from the code (e.g: for the "want"/expected
values of tests) and you wish to conveniently edit them, track them and
maintain them. Using Dir::Manifest you can put each in a
separate file in a directory, create a manifest file listing all valid
filenames/key and then say something like 'my $text =
$dir->text("deal24solution.txt", {lf => 1})'. And hopefully it will be done
securely and reliably.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Build.PL --installdirs=vendor

./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0


%files
%license LICENSE
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.1-3
- Perl 5.32 rebuild

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.1-2
- Add missing dependency

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.5-2
- Perl 5.30 rebuild

* Wed Apr 24 2019 Shlomi Fish <shlomif@cpan.org> 0.0.3-1
- Initial Fedora package based on the Mageia one.

