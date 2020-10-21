%global _dwz_low_mem_die_limit 0

Name:           reposurgeon
Version:        4.19
Release:        1%{?dist}
Summary:        SCM Repository Manipulation Tool
License:        BSD
URL:            http://www.catb.org/~esr/reposurgeon/
Source0:        http://www.catb.org/~esr/reposurgeon/%{name}-%{version}.tar.xz

BuildRequires:  asciidoctor
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  xmlto

BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/text/encoding/ianaindex)
BuildRequires:  golang(github.com/emirpasic/gods/sets/linkedhashset)
BuildRequires:  golang(github.com/anmitsu/go-shlex)
BuildRequires:  golang(github.com/kballard/go-shellquote)
BuildRequires:  golang(github.com/ianbruene/go-difflib/difflib)
BuildRequires:  golang(github.com/termie/go-shutil)
BuildRequires:  golang(gitlab.com/ianbruene/kommandant)
BuildRequires:  golang(gitlab.com/esr/fqme)

# Tests
BuildRequires:  golint
BuildRequires:  ShellCheck

Requires:       emacs-filesystem

%description
Reposurgeon enables risky operations that version-control systems don't want
to let you do, such as editing past comments and metadata and removing
commits. It works with any version control system that can export and import
git fast-import streams, including git, hg, fossil, bzr, CVS and RCS. It can
also read Subversion dump files directly and can thus be used to script 
production of very high-quality conversions from Subversion to any supported
DVCS.

%prep
%setup -q
# Set go build options
sed -i 's/^#GOFLAGS=-gcflags.*/GOFLAGS=-gcflags "-N -l" -ldflags "-B 0x\$\(shell head -c20 \/dev\/urandom|od -An -tx1|tr -d '\'' \\n'\'')"/g' Makefile

%build
export GOPATH=$(pwd):%{gopath}
export GO111MODULE=off

asciidoctor README.adoc NEWS.adoc

# preserve build order
make

%install
%make_install prefix=%{_prefix}

install -pDm644 reposurgeon-mode.el %{buildroot}%{_datadir}/emacs/site-lisp/reposurgeon-mode.el

# Use %%doc to install docs.
rm -frv %{buildroot}%{_docdir}

# Strip repobench
rm -f %{buildroot}%{_bindir}/repobench
rm -f %{buildroot}%{_mandir}/man1/repobench.1*

%check
export GOPATH=$(pwd):%{gopath}
export GO111MODULE=off

make check

%files
%doc *.html oops.svg
%license COPYING
%{_bindir}/%{name}
%{_bindir}/repocutter
%{_bindir}/repomapper
%{_bindir}/repotool
%{_datadir}/emacs/site-lisp/reposurgeon-mode.el
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/repocutter.1*
%{_mandir}/man1/repomapper.1*
%{_mandir}/man1/repotool.1*

%changelog
* Tue Sep 01 2020 Denis Fateyev <denis@fateyev.com> - 4.19-1
- Update to 4.19

* Tue Aug 18 2020 Denis Fateyev <denis@fateyev.com> - 4.17-1
- Switch to Go-based version
- Update to 4.17

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Maya Rashish <mrashish@redhat.com> - 3.47-3
- Fix tab/space inconsistency

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Denis Fateyev <denis@fateyev.com> - 3.47-1
- Update to 3.47

* Fri Aug 16 2019 Denis Fateyev <denis@fateyev.com> - 3.46-1
- Update to 3.46

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 Denis Fateyev <denis@fateyev.com> - 3.42-6
- Dropped deprecated python2 dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 Denis Fateyev <denis@fateyev.com> - 3.42-1
- Update to 3.42

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Denis Fateyev <denis@fateyev.com> - 3.40-1
- Update to 3.40

* Sat Sep 03 2016 Denis Fateyev <denis@fateyev.com> - 3.39-1
- Update to 3.39

* Mon Mar 21 2016 Denis Fateyev <denis@fateyev.com> - 3.37-1
- Update to 3.37

* Fri Mar 04 2016 Denis Fateyev <denis@fateyev.com> - 3.35-1
- Update to 3.35

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 04 2015 Christopher Meng <rpm@cicku.me> - 3.29-2
- Update to 3.29

* Sun Jul 19 2015 Christopher Meng <rpm@cicku.me> - 3.28-1
- Update to 3.28

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 Christopher Meng <rpm@cicku.me> - 3.19-1
- Update to 3.19

* Thu Sep 18 2014 Christopher Meng <rpm@cicku.me> - 3.12-1
- Update to 3.12
- Explicit svn:ignore patterns aren't recursive to lower directories; cope.
- A new 'ignores' command has obtions for translation of ignore files.
- The --noignores option has been retired.

* Thu Aug 28 2014 Christopher Meng <rpm@cicku.me> - 3.11-1
- Update to 3.11
- When converting SVN, ignore explicit .gitignores created by git-svn.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Christopher Meng <rpm@cicku.me> - 3.10-1
- Update to 3.10
- Finer control over filtering with caC flags.
- New setfield command for tweaking object attributes from lift scripts.
- The attribution-parsing code handles odd characters in names better now. 
- The filter command can operate on email addresses as well as names.
- New 'stamp' command to report action stamps of commits.
- New 'count' comment reports selection-set counts.
- New branchify_mapping option for renaming Subversion branches on analysis.
- New transcode command for moving metadata to UTF-8.
- New @dsc() function for selecting all descendants of a selection set.

* Fri Mar 21 2014 Christopher Meng <rpm@cicku.me> - 3.7-1
- Update to 3.7
- New --dedos option for filter command, to change \r\n line endings to \n.
- New append command for annotating comments.
- The 'b' search code has been changed to appropriately match non-commits.
- New form of 'graft' allows greater control over graft points.
- New =I selector to find non-UTF-8 commit metadata.
- Import stream comments led with # are preserved as passthroughs.
- Buggy text search of authors fields has been fixed.

* Thu Feb 20 2014 Christopher Meng <rpm@cicku.me> - 3.6-1
- Update to 3.6
- Major rewrite of the generic conversion makefile.
- Fixed a bug in the graft and unite commands.
- Single fossil or tag names now select as if surrounded by <>.
- Fixed more bugs in debranch.
- @amp() function useful for logic-gating in conjunctive expressions.
- New 'assign' command allows precomputation of expensive selections.
- There's an 'unassign' as well.
- exec/eval facility for custom Python extensions.
- path rename has a --relax and --force options to deal with oath collisions
- New --changelog option of coalesce can recognize FSF-style ChangeLog files.

* Thu Feb 13 2014 Christopher Meng <rpm@cicku.me> - 3.3-1
- Update to 3.3
- Set negation in selections with ~.
- @min() and @max() in selections.
- 'define' by itself lists macros.
- New 'deletes' option in the remove command.

* Wed Feb 05 2014 Christopher Meng <rpm@cicku.me> - 3.2-1
- Update to 3.2
- New path rename command.
- List and inspect now take either a leading or following selection.
- Text search selections can now have a B suffix to search blobs.
- Now possible to transplant fileops between commits using remove .. to.
- A date of the form <YYYY-mm-dd> selects all commits and tags that day.
- Macros can now be multiline.
- The filter command now has a --replace modifier to avoid regex overhead.
- Associated branches are renamed when a reset or tag is moved or deleted.
- Bug fix for off-by-one error in tags reporting.
- Many syntactic features of the language have changed incompatibly.
- Backward-incompatible language changes are documented on the manual page.
- 'expunge' and 'unite' commands have been incompatibly improved.
- New 'strip' command for generating test cases with blobs stripped out
- New 'reduce' command for topological reduction of test cases.
- The 'lint' command gets a test for the existence of multiple roots.
- Selecting a date or action stamp matching multiple commits now matches all.
- The surgical language now has a macro facility.
- "set canonicalize" is now effective during import stream reads.
- Introduced =O, =M, =F selectors for parentless, merge, and fork commits.
- The "multiline" modifier on edit is replaced by the =L selector.
- Selection-set evaluation now short-circuits predicates and is faster.
- Fixed a buggy test that caused the reader to choke on submodule links.

* Thu Nov 21 2013 Christopher Meng <rpm@cicku.me> - 2.42-1
- Update to 2.42
- Prevented crash when tagifying a mixed-branch commit.
- svn_no_autoignores -> svn_noautoignores.
- Ignore single-rev mergeinfos in Subversion, they're cherry-picks.

* Sat Nov 09 2013 Christopher Meng <rpm@cicku.me> - 2.41-1
- Update to 2.41
- Fixed a fatal bug when reading any symlink from a live Subversion repo.
- Added svn_no_autoignores option.

* Thu Aug 08 2013 Christopher Meng <rpm@cicku.me> - 2.40-1
- Update to 2.40
- Improvements in .gitignore processing.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Christopher Meng <rpm@cicku.me> - 2.39-2
- Add parallel make support.

* Fri May 24 2013 Christopher Meng <rpm@cicku.me> - 2.39-1
- Update to 2.39
- New 'tagify' command for tagifying empty commits.
- Correctness fixes for deletion edge cases.

* Fri May 10 2013 Christopher Meng <rpm@cicku.me> - 2.38-1
- Update to 2.38
- Significant improvements to Subversion branch link detection.
- New 'reparent' command for modifying the DAG.
- Fixes for two minor crash bugs in handling of malformed commands.

* Fri Apr 26 2013 Christopher Meng <rpm@cicku.me> - 2.37-1
- Update to 2.37
- No more tree pollution on branches deduced from file copies.

* Sun Apr 21 2013 Christopher Meng <rpm@cicku.me> - 2.35-1
- Update to 2.35
- New "manifest" command.
- Path-matching now has @ to require all paths in a commit to match.

* Wed Apr 17 2013 Christopher Meng <rpm@cicku.me> - 2.33-1
- Update to 2.33

* Sun Apr 07 2013 Christopher Meng <rpm@cicku.me> - 2.32-1
- Initial package.
