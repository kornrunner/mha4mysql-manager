Summary: Master High Availability Manager and Tools for MySQL, Manager Package
Name: mha4mysql-manager
Version: 0.59
Release: 0%{?dist}
License: GPL v2
Vendor: DeNA Co.,Ltd.
Group: Manager
URL: http://code.google.com/p/mysql-master-ha/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl(Config::Tiny)
BuildRequires: perl(Log::Dispatch)
BuildRequires: perl(Parallel::ForkManager)
BuildRequires: perl(DBD::mysql)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires: perl(Module::Install)
BuildRequires: mha4mysql-node > 0.54
Requires: perl(Config::Tiny)
Requires: perl(Log::Dispatch)
Requires: perl(Parallel::ForkManager)
Requires: mha4mysql-node >= 0.54
Requires: perl(DBD::mysql)
Source0: mha4mysql-manager-%{version}.tar.gz

%description
%{summary}.

%prep
%setup -q -n mha4mysql-manager-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS="vendor" INSTALLVENDORLIB=%{?perl_install_vendor_lib}
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -a \( -name perllocal.pod -o -name .packlist \
  -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

for brp in %{_prefix}/lib/rpm/%{_build_vendor}/brp-compress \
  %{_prefix}/lib/rpm/brp-compress
do
  [ -x $brp ] && $brp && break
done

find $RPM_BUILD_ROOT -type f \
| sed "s@^$RPM_BUILD_ROOT@@g" \
> %{name}-%{version}-%{release}-filelist

if [ "$(cat %{name}-%{version}-%{release}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root,-)

%changelog
* Tue Sep 10 2019 Boris Momčilović <boris.momcilovic@gmail.com>
- MasterRotate.pm: notify if no need to change master, fixup
- ServerManager.pm: fixup masterha_check_repl
- MasterRotate.pm: notify if no need to change master
- MasterMonitor.pm: call things their names
- HealthCheck.pm: spelling
- MasterRotate.pm: Repllicate_Do_DB and Replicate_Ignore_DB shoud be same
- Add missing rpm build requirements
- Version 0.59

* Thu Mar 22 2018 Kenny.Gryp <kenny@goss.be>
- Several bugfixes
- IPV6 support
- super_read_only support
- enforce_storage_engine support
- Version 0.58
- With the help of Marcelo Altmann <marcelo.altmann@percona.com>

* Sun May 31 2015 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- (Note: All changelogs are written here: http://code.google.com/p/mysql-master-ha/wiki/ReleaseNotes )
- Version 0.57

* Tue Apr 1 2014 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.56

* Wed Dec 12 2012 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.55

* Sat Dec 1 2012 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.54

* Mon Jan 9 2012 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.53

* Fri Sep 16 2011 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.52

* Thu Aug 18 2011 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.51

* Sat Jul 23 2011 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.50

