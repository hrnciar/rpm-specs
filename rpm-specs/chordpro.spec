# -*- rpm-spec -*-

%define FullName App-Music-ChordPro

Name: chordpro
Summary: Print songbooks (lyrics + chords)
License: Artistic 2.0
Version: 0.974.1
Release: 6%{?dist}
Source: https://cpan.metacpan.org/authors/id/J/JV/JV/%{FullName}-%{version}.tar.gz
URL: https://www.chordpro.org

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

# This package would provide many (perl) modules, but these are
# not intended for general use.
%global __provides_exclude_from /*\\.pm$
%global __requires_exclude App::Music::ChordPro

Requires: perl(:VERSION) >= 5.10.1
Requires: perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

Requires: perl(App::Packager)               >= 1.430
Requires: perl(PDF::API2)                   >= 2.036
Requires: perl(Text::Layout)                >= 0.016
Requires: perl(JSON::PP)                    >= 2.27203
Requires: perl(String::Interpolate::Named)  >= 0.05
Requires: perl(File::LoadLines)             >= 0.02
Requires: perl(Image::Info)                 >= 1.41

BuildRequires: make
BuildRequires: perl(App::Packager)               >= 1.430
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)         >= 6.76
BuildRequires: perl(File::LoadLines)             >= 0.02
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Hash::Util)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Image::Info)                 >= 1.41
BuildRequires: perl(JSON::PP)                    >= 2.27203
BuildRequires: perl(PDF::API2)                   >= 2.036
BuildRequires: perl(String::Interpolate::Named)  >= 0.05
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Layout)                >= 0.016
BuildRequires: perl(base)
BuildRequires: perl(constant)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
ChordPro will read a text file containing the lyrics of one or many
songs plus chord information. ChordPro will then generate a
photo-ready, professional looking, impress-your-friends sheet-music
suitable for printing on your nearest printer.

To learn more about ChordPro, look for the man page or do
chordpro --help for the list of options.

ChordPro is a rewrite of the Chordii program.

For more information about ChordPro, see https://www.chordpro.org.

%prep
%setup -q -n %{FullName}-%{version}

# Remove Wx stuff. Not yet functional.
rm -fr lib/App/Music/ChordPro/Wx*
# And adjust the MANIFEST.
perl -i -ne 'print $_ unless /Wx/' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test

%install

# Short names for our libraries.
%global share %{_datadir}/%{name}-%{version}

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
echo "# Placeholder" > %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
mkdir -p %{buildroot}%{share}/lib
mkdir -p %{buildroot}%{_bindir}

# Create lib dirs and copy files.
find blib/lib -type f -name .exists -delete
find blib/lib -type d -printf "mkdir %{buildroot}%{share}/lib/%%P\n" | sh -x
find blib/lib ! -type d -printf "install -p -m 0644 %p %{buildroot}%{share}/lib/%%P\n" | sh -x

for script in chordpro
do

  # Create the main scripts.
  echo "#! /usr/bin/perl" > %{buildroot}%{_bindir}/${script}
  sed -e "s;# use FindBin.;use lib qw(%{share}/lib;" \
           -e "/FindBin/d;" \
    < script/${script} >> %{buildroot}%{_bindir}/${script}
  chmod 0755 %{buildroot}%{_bindir}/${script}

  # And its manual page.
  mkdir -p %{buildroot}%{_mandir}/man1
  pod2man blib/script/${script} > %{buildroot}%{_mandir}/man1/${script}.1

done
%{_fixperms} %{buildroot}/*

# End of install section.

%files
%doc CHANGES README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{share}/
%{_bindir}/chordpro
%{_mandir}/man1/chordpro*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.974.1-6
- Perl 5.32 rebuild

* Mon Mar 23 2020 Johan Vromans <jvromans@squirrel.nl> - 0.974.1-5
- Add perl(Hash::Util) build dep for Rawhide.

* Sun Mar 22 2020 Johan Vromans <jvromans@squirrel.nl> - 0.974.1-4
- Incorporate reviewer feedback.
- Upgrade to upstream.

* Thu Feb 27 2020 Johan Vromans <jvromans@squirrel.nl> - 0.974-3
- Incorporate reviewer feedback.

* Tue Feb 25 2020 Johan Vromans <jvromans@squirrel.nl> - 0.974-2
- Incorporate reviewer feedback.

* Sun Feb 02 2020 Johan Vromans <jvromans@squirrel.nl> - 0.974-1
- Initial Fedora package.
