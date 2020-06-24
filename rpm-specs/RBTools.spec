%{!?python2_sitelib: %global python2_sitelib %{python_sitelib}}

Name:           RBTools
Version:        1.0.3
Release:        2%{?dist}
Summary:        Tools for use with ReviewBoard

License:        MIT
URL:            http://www.reviewboard.org
Source0:        http://downloads.reviewboard.org/releases/%{name}/1.0/%{name}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?rhel} == 7
BuildRequires:  python36-devel
BuildRequires:  python36-setuptools
Requires:       python36-colorama
Requires:       python36-setuptools
Requires:       python36-simplejson
Requires:       python36-six >= 1.8.0
Requires:       python36-tqdm
Requires:       python36-texttable
%else
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-colorama
Requires:       python3-setuptools
Requires:       python3-simplejson
Requires:       python3-six >= 1.8.0
Requires:       python3-tqdm
Requires:       python3-texttable
Recommends:     bash-completion
%endif

### Patches ###


# Upstream

%description
RBTools provides client tools for interacting with a ReviewBoard
code-review server.

%prep
%autosetup -p1 -n %{name}-%{version}

rm -Rf %{name}*.egg-info

%build
%{py3_build}


%install
%{py3_install}

# Install bash and zsh completion scripts
install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d/
cp rbtools/commands/conf/rbt-bash-completion \
   %{buildroot}%{_sysconfdir}/bash_completion.d/rbt

install -d -m 755 %{buildroot}%{_datarootdir}/zsh/site-functions/
cp rbtools/commands/conf/_rbt-zsh-completion \
   %{buildroot}%{_datarootdir}/zsh/site-functions/_rbt

 
%files
%doc AUTHORS NEWS README.md
%{_bindir}/rbt
%{_sysconfdir}/bash_completion.d/
%{_datarootdir}/zsh/site-functions/_rbt
%{python3_sitelib}/rbtools/
%{python3_sitelib}/RBTools*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.9

* Mon Apr 27 2020 Stephen Gallagher <sgallagh@redhat.com> - 1.0.3-1
- Update to RBTools 1.0.3
- https://www.reviewboard.org/docs/releasenotes/rbtools/1.0.3/

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Stephen Gallagher <sgallagh@redhat.com> - 1.0.2-1
- Update to RBTools 1.0.2
- https://www.reviewboard.org/docs/releasenotes/rbtools/1.0.2/
- Build against Python 3.6 on EPEL 7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0.1-1
- Update to RBTools 1.0.1
- Fixed tracking branch detection with Git

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0-2
- Include missing python dependencies

* Fri Jun 29 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.0-1
- Update to RBTools 1.0
- https://www.reviewboard.org/docs/releasenotes/rbtools/1.0/

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Stephen Gallagher <sgallagh@redhat.com> - 0.7.11-1
- Update to 0.7.11
- Fix sitelib macro for Fedora 28

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.7.10-1
- Update to RBTools 0.7.10
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7.9/
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7.10/

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.7.8-1
- Update to RBTools 0.7.8
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7.8/

* Fri Jan 06 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.7.7-2
- Add dependency on python-tqdm

* Mon Nov 28 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.7.7-1
- New upstream release 0.7.7
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7.7/

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 27 2016 Stephen Gallagher <sgallagh@redhat.com> 0.7.6-1
- New upstream release 0.7.6
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7.6/

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Stephen Gallagher <sgallagh@redhat.com> 0.7.5-2
- New upstream release 0.7.5
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7.5/

* Fri Jun 19 2015 Stephen Gallagher <sgallagh@redhat.com> 0.7.4-2
- Fix python-six requirement to set the minimum version to 1.4

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Stephen Gallagher <sgallagh@redhat.com> 0.7.4-1
- New upstream release 0.7.4
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7.4/

* Fri May 29 2015 Stephen Gallagher <sgallagh@redhat.com> 0.7.3-1
- New upstream release 0.7.3
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7.3/

* Tue Mar 10 2015 Stephen Gallagher <sgallagh@redhat.com> 0.7.2-1
- New upstream release 0.7.2
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7.2/

* Fri Feb 06 2015 Stephen Gallagher <sgallagh@redhat.com> 0.7.1-1
- New upstream release 0.7.1
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7.1/

* Tue Jan 20 2015 Stephen Gallagher <sgallagh@redhat.com> 0.7-2
- Relax python-six requirement

* Mon Jan 19 2015 Stephen Gallagher <sgallagh@redhat.com> 0.7-1
- New upstream release 0.7
- https://www.reviewboard.org/docs/releasenotes/rbtools/0.7/
- API Caching for performance enhancements
- Support for command aliases
- 'rbt land' tool will now handle landing Git commits for upstream
- 'rbt post' can now exclude some files (such as autogenerated ones)
  from the review
- Support for Microsoft Team Foundation Server (when used with
  Review Board Power Pack on the server-side

* Mon Nov 17 2014 Stephen Gallagher <sgallagh@redhat.com> 0.6.3-2
- Actually apply the "-C" patch

* Thu Nov 13 2014 Stephen Gallagher <sgallagh@redhat.com> 0.6.3-1
- New upstream release 0.6.3
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.6.3/
- Include upstream patch adding 'rbt patch -C' to automatically commit a patch
  to a local git repository.

* Mon Jul 07 2014 Stephen Gallagher <sgallagh@redhat.com> 0.6.2-1
- New upstream release 0.6.2
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.6.2/

* Tue Jun 10 2014 Stephen Gallagher <sgallagh@redhat.com> 0.6.1-1
- New upstream release 0.6.1
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.6.1/

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Stephen Gallagher <sgallagh@redhat.com> 0.6-2
- Properly generate parent diffs in git
- Switch to fuzzy search in setup-repo to match repository path
- Fix perforce options access
- Fix -I with svn repositories

* Tue Apr 08 2014 Stephen Gallagher <sgallagh@redhat.com> 0.6-1
- New upstream release 0.6
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.6/

* Wed Feb 05 2014 Stephen Gallagher <sgallagh@redhat.com> 0.5.7-1
- New upstream release 0.5.7
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.5.7/
- New upstream release 0.5.6
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.5.6/

* Wed Jan 15 2014 Stephen Gallagher <sgallagh@redhat.com> 0.5.5-1
- New upstream release 0.5.5
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.5.5/
- New upstream release 0.5.4
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.5.4/
- Deprecation:
  * post-review is deprecated (and has been for a while). It now shows a
    deprecation warning in order to remind me to use rbt post.
- Bug Fixes:
  * rbt patch:
    * rbt patch no longer fails to commit on Git if there are untracked files.
    * Fixed committing changes when the description has unicode characters.
    * Fixed compatibility with Review Board 2.0 beta.
  * rbt post:
    * Fixed R1:R2 syntax for --revision-range for Git repositories.
    * Fixed name-based lookups for repositories with Subversion.
  * rbt setup-repo:
    * Fixed error output when failing to write the .reviewboardrc file.
  * post-review:
    * Added --svn-show-copies-as-adds to post-review.

* Mon Jan 06 2014 Stephen Gallagher <sgallagh@redhat.com> - 0.5.3-1
- New upstream release 0.5.3
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.5.3/

* Thu Aug 15 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.5.2-1
- New upstream release 0.5.2
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.5.2/

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.5.1-1
- New upstream release 0.5.1
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.5.1/
- Drop upstreamed ez_setup patch
- New Features:
    * Improved the readability of rbt status output
    * Added a --repository-type option to most commands
    * Added a --list-repository-types option to post-review
    * Added a new rbt list-repo-types command
    * Third-parties can now write new SCM support by creating Python packages
      leveraging Python entry points
- API Client Changes:
    * Added an API Client method for retrieving resources from a path
    * Add a get_or_create_draft method to the API
    * Restructured the API Client internally
- Bug Fixes:
    * Fixed crash when copying old post-review cookies for use with rbt
    * rbt commands will now properly generate diffs with moved files
    * Fixed references to non-existent variables in rbt patch
    * Fixed rbt post for Perforce repositories
    * Fixed rbt post and rbt diff for Subversion and Bazaar
    * Fixed post-review and rbt when used for Perforce paths
    * Fixed error handling when posting a review request
- Packaging Changes:
    * Conditionalize ez_setup

* Tue Mar 19 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.5-1
- New upstream release 0.5
- http://www.reviewboard.org/docs/releasenotes/rbtools/0.5/
- New Features:
    * API Client
        * A new Python API Client has been introduced for communication with
          the Review Board Web API
    * rbt
        * This is the initial release of our new command line tool, rbt
        * Provides access to useful sub-commands which interact with local
          source code repositories and Review Board
        * Currently considered beta
        * See release notes link for detailed information
- Bug Fixes
    * Perforce:
        * Fix treating an SVN repository as Perforce by mistake
        * Fix diff generation with unedited files in Perforce
        * Gracefully handle no-match in p4 info regex
    * ClearCase:
        * Support posting review requests in ClearCase snapshot view
    Subversion:
        * Don’t block waiting for user input from svn

* Mon Jan 28 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.4.3-1
- New upstream release 0.4.3
- http://www.reviewboard.org/docs/releasenotes/dev/rbtools/0.4.3/
- New Features:
    * Added support for posting from Bazaar repositories
    * Passing --basedir to post-review will override the computed base
      directory used for Subversion diffs
    * Added better support for moved files in Perforce
- Bug Fixes:
    * General:
      * Fixed problems authenticating with the server when anonymous access is
        disabled
      * Fixed loading settings from the user’s ~/.reviewboardrc when it’s the
        only .reviewboardrc in the search path
      * Fixed a crash when the user’s home directory isn’t writable
      * Added a fallback when failing to get the API version from a Review
        Board server
      * The "Username" prompt is now printed to stderr instead of stdout, to
        match the “Password” prompt’s inputted text
      * Unicode URLs are now encoded as UTF-8, preventing an encoding conflict
        when talking to Review Board
    * Git:
      * Git diffs no longer contain move/rename information if the Review Board
        server doesn’t support it
    * Mercurial:
      * Fixed --guess-summary when it has newline characters in it
    * Subversion:
      * Fixed problems generating diffs containing deleted files

* Fri Nov 16 2012 - Stephen Gallagher <sgallagh@redhat.com> - 0.4.2-1
- New upstream release 0.4.2
- http://www.reviewboard.org/docs/releasenotes/dev/rbtools/0.4.2/
- New Features:
-  * The .post-review-cookies.txt file is now made readable only by the calling
     user, improving security
-  * Improved debug output
-  * Updated our Plastic support for Plastic 4.0. This is no longer
     compatible with previous versions
-  * A revision to diff against can now be specified when using hgsubversion
- Bug Fixes:
-  * General:
-    * Using UTF-8 in the summary or description no longer breaks
-    * The GNU diff error no longer mentions Subversion specifically
-    * Posting a diff to a submitted review request now displays an error
       instead of reopening the review request
-  * Clearcase:
-    * Fixed base path generation for Clear Case
-  * Git:
-    * Fix issues when running post-review within a git submodule with recent
       Git revisions
-    * Git diffs no longer include diffs from submodules, preventing useless
       diffs from being created
-    * post-review no longer breaks when run from a detached Git HEAD
-  * Mercurial:
-    * Fixed bailing on harmless warnings when running hg commands
-    * Fixed path calculation for hgsubversion when the path contains a
       username
-  * Subversion:
-    * Scanning for the right repository is much faster now when there are lots
       of Subversion repositories on the server
-    * Fix handling of revisions with deleted files for Subversion
-    * Handle modifications inside moved/copied directories for Subversion

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 29 2012 - Stephen Gallagher <sgallagh@redhat.com> - 0.4.1-1
- New upstream release 0.4.1
- http://www.reviewboard.org/docs/releasenotes/dev/rbtools/0.4.1/
- Fixed Python 2.4 compatibility
- Fixed --diff-filename=- with --username and --password

* Mon Feb 27 2012 - Stephen Gallagher <sgallagh@redhat.com> - 0.4.0-1
- New upstream release 0.4.0
- http://www.reviewboard.org/docs/releasenotes/dev/rbtools/0.4/
- Features (post-review):
-   Defaults for many parameters can now be specified in .reviewboardrc
-   Added a --disable-proxy option for disabling the HTTP(S) proxy server
- Bugfixes (post-review):
-   Fixed authentication problems when accessing the API
-   Shows a nicer error when trying to update someone else's review request
-   Fixed crashes when the home directory wasn’t writable
-   Fixed using --diff-filename=- without a valid cookie
-   Fixed the link to the Repository Configurations documentation
- Bugfixes (Git):
-   Fixed problems when using --repository-url
- Bugfixes (Mercurial):
-   Make Mercurial handle the case where there are no outgoing changes
-   Improve merge support in order to generate better diffs
- Bugfixes (Perforce):
-   Using --revision-range on Perforce now provides better errors
-   Display an informative error if GNU diff isn’t installed
-   Fix handling of new files in post-commit scenarios

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 27 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.3.4-1
- New upstream 0.3.4 release
- http://www.reviewboard.org/docs/releasenotes/dev/rbtools/0.3.4/
- New Features:
-   post-review:
-     Added a --change-description option for setting the Change Description
      text on drafts
- Bugfixes:
-   post-review:
-     Newlines in summaries on Git are now converted to spaces, preventing
      errors when using --guess-summary
-     Fixed authentication failures when accessing a protected /api/info/
      URL. This was problematic particularly on RBCommons
-     Fixed diff upload problems on Python 2.7

* Mon Aug 22 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.3.3-1
- New upstream 0.3.3 release
- http://www.reviewboard.org/docs/releasenotes/dev/rbtools/0.3.3/
- Notable Changes:
-   Rewrote the Clear Case implementation to be cleaner, more maintainable,
    and less buggy
- New Features:
-   post-review:
-      Added --http-username and --http-password for providing defaults for
       Basic HTTP Authentication
-   Clear Case:
-      Added proper support for --tracking-branch and --revision-range
-      Clear Case configuration has moved to .reviewboardrc
-   Git:
-      Added automatic parent diff determination when using --revision-range
-      Added support for working against bare repositories when using
       --revision-range
-      Enhanced --revision-range to take any valid Git revisions
-      Support --repository-url for overriding the git origin URL
-   Mercurial:
-      Added support for --guess-summary and --guess-description
-      Allow a single revision to be passed to --revision-range
-   Subversion:
-      Added support for --svn-changelist for specifying SVN changelists
- Bug Fixes:
-   post-review:
-      Fixed authentication problems with some versions of Review Board
-   Clear Case:
-      The view is properly recognized
-      Removed the dependency on xargs and cygwin
-      Fixed breakages with binary files
-      Removed support for --label, which was useless
-      Running just post-review will now produce a working diff of checked
       out files
-      Diffs generate properly now under Windows
-      The diffs no longer hard-code a fake date, but instead use the real
       time/date of the file
-      Files that were renamed no longer breaks the diff. OID/UUIDs are used
       instead of file paths
-      Fixed diff generation to use the diff program instead of hand-crafting
       the diffs
-      Running with --revision-range with paths that don't exist no longer
       produces unreadable IOException errors
-   Git:
-      Use real URLs when using git prefixes
-      Fixed compatibility with versions of Git older than 1.6
-      Added compatibility with msysgit
-      The correct SVN remote tracking branch is now used for git-svn
       repositories
-   Mercurial:
-      Fixed an error when posting inside a Mercurial branch
-   Perforce:
-      Fixed Review Board version detection when checking for Perforce
       changeset support. This forced usage of the old API, preventing the new
       API from being used, which prevented usage with Review Board 1.6
-   Subversion:
-      Lines starting with --- and +++ in diffs that aren't diff control lines
       no longer results in broken diffs

* Wed Feb 09 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.3.2-1
- New upstream 0.3.2 release
- Fixed using Perforce change numbers with Review Board 1.5.2
- Fixed parsing CVSROOTs with :ext: schemes not containing a username
- Mercurial no longer takes precedence over Perforce if a valid Mercurial
- user configuration is found

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.3.1-1
- New upstream 0.3.1 release
- Added a .reviewboardrc setting for specifying the repository to use
- Fixed a crash when using the old, deprecated API and accessing an existing
- review request

* Tue Feb 01 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.3-1
- New upstream release
- Support for new ReviewBoard 1.5.x API
- Support for Plastic SCM
- Full release notes:
- http://www.reviewboard.org/docs/releasenotes/dev/rbtools/0.3/

* Fri Jul 30 2010 Stephen Gallagher <sgallagh@redhat.com> - 0.2-6
- Rebuild for python 2.7

* Mon Apr 19 2010 Stephen Gallagher <sgallagh@redhat.com> - 0.2-5
- Update to 0.2 final release

* Tue Apr 06 2010 Stephen Gallagher <sgallagh@redhat.com> - 0.2-3.rc1
- Add runtime requirement for python-setuptools

* Mon Apr 05 2010 Stephen Gallagher <sgallagh@redhat.com> - 0.2-2.rc1
- Remove git-patchset patch
- Add patch to check for GNU diff
- Add patch to give more useful error messages on failure

* Mon Mar 15 2010 Stephen Gallagher <sgallagh@redhat.com> - 0.2-1.rc1
- Import upstream release 0.2rc1
- Add patches from upstream
- Add patch to support git patchsets
