%global gem_name sup

Summary: A console-based email client written in ruby
Name: rubygem-%{gem_name}
Version: 0.22.1
Release: 6%{?dist}
License: GPLv2+
URL: http://sup.rubyforge.org/
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
# Revert dependency on ncursesw. The downside is incorrect wide character support.
# TODO: Resurrect rubygem-ncursesw (rhbz#597709).
# https://github.com/sup-heliotrope/sup/commit/c52016368e0456baf1ee97d25304b703da542cec
Patch1: rubygem-sup-Revert-Remove-all-ncursesw-warnings-since-it-s-a-har.patch

Requires: ruby(ncurses)
Requires: xapian-bindings-ruby

BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: xapian-core-devel
BuildRequires: rubygems-devel
BuildRequires: ncurses-devel
BuildRequires: xapian-bindings-ruby
BuildRequires: zlib-devel
BuildRequires: rubygem-rake

BuildArch: noarch

Provides: %{gem_name} = %{version}

%package doc
Summary: Documentation for %{name}
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%description
Sup is a console-based email client for people with a lot of email. It
supports tagging, very fast full-text search, automatic contact-list
management, and more. If you're the type of person who treats email as an
extension of your long-term memory, Sup is for you.  Sup makes it easy to: -
Handle massive amounts of email.  - Mix email from different sources: mbox
files (even across different machines), Maildir directories, IMAP folders, POP
accounts, and GMail accounts.  - Instantaneously search over your entire email
collection. Search over body text, or use a query language to combine search
predicates in any way.  - Handle multiple accounts. Replying to email sent to
a particular account will use the correct SMTP server, signature, and from
address.  - Add custom code to handle certain types of messages or to handle
certain types of text within messages.  - Organize email with user-defined
labels, automatically track recent contacts, and much more!  The goal of Sup
is to become the email client of choice for nerds everywhere.

%prep
%setup -q -n %{gem_name}-%{version}
%patch1 -p1

# Remove unnecessary fake extension module
sed -i '/s.extensions =/ s/^/#/' ../%{gem_name}-%{version}.gemspec

# Relax rubygem-chronic dependency.
sed -i '/chronic/ s/0.9.1/0.9/' ../%{gem_name}-%{version}.gemspec

# Remove dependency on xapian-full and ncursesw
sed -i '/xapian-full/ s/^/#/' ../%{gem_name}-%{version}.gemspec
sed -i '/ncursesw/ s/^/#/' ../%{gem_name}-%{version}.gemspec

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
mv .%{gem_dir}/* %{buildroot}%{gem_dir}
mv .%{_bindir}/* %{buildroot}%{_bindir}

%files
%dir %{gem_instdir}
%{_bindir}/sup
%{_bindir}/sup-add
%{_bindir}/sup-config
%{_bindir}/sup-dump
%{_bindir}/sup-recover-sources
%{_bindir}/sup-sync
%{_bindir}/sup-tweak-labels
%{_bindir}/sup-import-dump
%{_bindir}/sup-psych-ify-config-files
%{_bindir}/sup-sync-back-maildir
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/bin
%{gem_instdir}/lib
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/CONTRIBUTORS
%{gem_instdir}/Gemfile
%{gem_instdir}/HACKING
%{gem_instdir}/History.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/README.md
%{gem_instdir}/ReleaseNotes
%{gem_instdir}/test
%{gem_instdir}/devel
%{gem_instdir}/contrib
%{gem_instdir}/doc
%{gem_instdir}/man
%{gem_instdir}/ext

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Pavel Valena <pvalena@redhat.com> - 0.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Pavel Valena <pvalena@redhat.com> - 0.22.1-1
- Update to sup 0.22.1.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Jun Aruga <jaruga@redhat.com> - 0.21.0-5
- Relax rubygem-mime-types dependency. (rhbz#1357017)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 02 2015 Vít Ondruch <vondruch@redhat.com> - 0.21.0-3
- Relax rubygem-chronic dependency.
- Temporary use ncurses, until rubygem-ncursesw is in Fedora.
- Small cleanup.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.21.0-1
- Add new source tarball and updated dependecies

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.10.2-11
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.10.2-8
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 14 2010 Shreyank Gupta <sgupta@redhat.com> - 0.10.2-5
- Added Provides: rubygem(%%{gemname}) = %%{version}

* Mon Jun 14 2010 Shreyank Gupta <sgupta@redhat.com> - 0.10.2-4
- Removed redundant versions from Requires.
- Moving %%{gemdir}/bin/* to %%{_bindir}
- Excluded lib/ncurses.rb
- Renamed package to rubygem-sup

* Fri Jun 11 2010 Shreyank Gupta <sgupta@redhat.com> - 0.10.2-3
- Removed require 'xapian-full' and 'ncursesw' from gemspec

* Wed Jun 09 2010 Shreyank Gupta <sgupta@redhat.com> - 0.10.2-2
- Moving %%geminstdir/bin/* instead of %%gemdir/bin/* to %%_bindir
- Requires xapian-bindings-ruby

* Mon Jun 07 2010 Shreyank Gupta <sgupta@redhat.com> - 0.10.2-1
- Initial package
